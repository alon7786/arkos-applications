import os

from arkos.backup import BackupController


class WallabagBackup(BackupController):
    def get_config(self, site):
        return []
    
    def get_data(self, site):
        return []
    
    def pre_backup(self, site):
        pass
    
    def post_backup(self, site):
        pass
    
    def pre_restore(self):
        pass
    
    def post_restore(self, site, dbpasswd):
        with open(os.path.join(site.path, 'inc/poche/config.inc.php'), 'r') as f:
            ic = f.readlines()
        oc = []
        for l in ic:
            if 'define (\'STORAGE_PASSWORD\'' in l:
                l = '@define (\'STORAGE_PASSWORD\', \''+dbpasswd+'\');'
                oc.append(l)
            else:
                oc.append(l)
        with open(os.path.join(site.path, 'inc/poche/config.inc.php'), 'w') as f:
            f.writelines(oc)
