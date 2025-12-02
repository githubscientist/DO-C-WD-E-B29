import os
import datetime
import shutil


class BackupManager:
    def __init__(self, sourceDir, destDir):
        self.sourceDir = sourceDir
        self.destDir = destDir

    def performBackup(self):
        # check if source directory exists
        # If not, print an error and break
        if not os.path.exists(self.sourceDir):
            print("Source directory is not found. Hence, backup cannot be performed")
            return

        # generate the name of the backup file
        timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = "backup_" + timestamp

        # check if the destination directory exists
        if not os.path.exists(self.destDir):
            # If not, create a destination directory
            os.makedirs(self.destDir)

        # compress or zip the folder
        # copy the file to the destination directory
        shutil.make_archive(
            base_name=filename,
            format="zip",
            root_dir=self.destDir,
            base_dir=self.sourceDir
        )

        # print that the backup is done!
        print("Backup is successfully done!")


backupManager = BackupManager(
    "/Users/sathish/Desktop/DO-C-WD-E-B29/logs", "/Users/sathish/Desktop/DO-C-WD-E-B29/backups/")
backupManager.performBackup()
