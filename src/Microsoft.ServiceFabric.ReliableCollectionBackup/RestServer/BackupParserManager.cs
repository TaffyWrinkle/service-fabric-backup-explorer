// ------------------------------------------------------------
// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT License (MIT). See License.txt in the repo root for license information.
// ------------------------------------------------------------

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using log4net;
using System.Reflection;

using Microsoft.ServiceFabric.ReliableCollectionBackup.Parser;

namespace Microsoft.ServiceFabric.ReliableCollectionBackup.RestServer
{
    /// <summary>
    /// Wrapper around BackupParser for enumerating over transactions.
    /// </summary>
    public class BackupParserManager : IDisposable
    {
        private static readonly ILog log = LogManager.GetLogger(MethodBase.GetCurrentMethod().DeclaringType);
        public BackupParserManager(BackupParser backupParser)
        {
            this.BackupParser = backupParser;
            // todo : take NumMaxTransactionsInMemory from config.
            this.transactionsQueue = new BlockingCollection<NotifyTransactionAppliedEventArgs>(NumMaxTransactionsInMemory);
            this.BackupParser.TransactionApplied += (sender, args) =>
            {
                if (transactionsQueue.Count < NumMaxTransactionsInMemory)
                {
                    transactionsQueue.Add(args);
                    Console.WriteLine("{0} : TransactionId {1} , CommitSequenceNumber {2}, Changes {3}", transactionsQueue.Count, args.TransactionId, args.CommitSequenceNumber, args.Changes.Count());
                }
            };
        }

        /// <summary>
        /// Starts parsing the backup without blocking.
        /// </summary>
        /// <returns>Task representing the asynchronous parsing of backup.</returns>
        public Task StartParsing()
        {
            if (this.parsingTask == null)
            {
                // todo : take cancellation timeout from config.
                this.parsingTask = this.BackupParser.ParseAsync(CancellationToken.None);
            }

            return parsingTask;
        }

        /// <summary>
        /// Try to give all transactions.
        /// </summary>
        /// <returns>Returns list of transactions</returns>
        public List<NotifyTransactionAppliedEventArgs> GetTransactions()
        {
            lock(queueLock)
            {
                return transactionsQueue.AsEnumerable<NotifyTransactionAppliedEventArgs>().ToList<NotifyTransactionAppliedEventArgs>();
            }
        }

        ///// <summary>
        ///// Checks if it has any unconsumed transactions.
        ///// </summary>
        ///// <returns>True if we have more transactions otherwise false.</returns>
        //public bool HasNextTransaction()
        //{
        //    return this.transactionsQueue.Count > 0;
        //}

        /// <summary>
        /// Checks if parsing operation has finished.
        /// If this parsing has finished and <see cref="HasNextTransaction"/> also returns false,
        /// then we will not have any more transactions in future.
        /// </summary>
        /// <returns></returns>
        public bool HasParsingFinished()
        {
            return this.parsingTask.IsCompleted;
        }

        /// <summary>
        /// Dispose the Backup manager
        /// </summary>
        public void Dispose()
        {
            this.BackupParser.Dispose();
        }

        internal BackupParser BackupParser { get; private set; }
        private Task parsingTask;
        private BlockingCollection<NotifyTransactionAppliedEventArgs> transactionsQueue;
        // lock is used for taking N items from transactionsQueue atomically across concurrent requests.
        private static Object queueLock = new Object();
        private const int NumMaxTransactionsInMemory = 1000000;
        //bool blockOnQueueFull = false;
    }
}