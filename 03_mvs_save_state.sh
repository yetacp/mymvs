#!/bin/bash
# Move ultimo backup para penultimo
if [ -f dasd_shadows.tar.gz ]; then
  NOW=`date +%Y%m%d_%H%M%S`
  BACKUP="backups/dasd_shadows_${NOW}.tar.gz"
  mv dasd_shadows.tar.gz ${BACKUP}
fi
# Copia ramdisk para ultimo backup
cd ./shadows
tar -czf ../dasd_shadows.tar.gz *
