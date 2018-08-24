// ------------------------------------------------------------
// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT License (MIT). See License.txt in the repo root for license information.
// ------------------------------------------------------------

using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace Microsoft.ServiceFabric.Tools.RCBackupGenerator
{
    class Program
    {
        static void Main(string [] args)
        {
            var backupGenerator = new ComplexTypesBackupGenerator();
            var path = Path.Combine(Directory.GetCurrentDirectory(), Guid.NewGuid().ToString("N"));
            backupGenerator.GenerateUserData(path).GetAwaiter().GetResult();
            Console.WriteLine("Generated backup at {0}", path);
        }
    }
}
