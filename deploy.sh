/usr/bin/rsync --progress --archive --recursive --delete --exclude-from=".rsyncignore" ./ fbinsect@192.168.0.100:UQ-REIT484X-Project/
/usr/bin/rsync --progress --archive --recursive --delete --exclude-from=".rsyncignore" ./ jntwo@192.168.0.101:UQ-REIT484X-Project/

# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./pipeline.py fbinsect@192.168.0.100:UQ-REIT484X-Project/pipeline.py
# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./api_rpi.py fbinsect@192.168.0.100:UQ-REIT484X-Project/api_rpi.py
# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./config.json fbinsect@192.168.0.100:UQ-REIT484X-Project/config.json
# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./preprocessor.py fbinsect@192.168.0.100:UQ-REIT484X-Project/preprocessor.py

# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./api_jetson.py jntwo@192.168.0.101:UQ-REIT484X-Project/api_jetson.py
# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./config.json jntwo@192.168.0.101:UQ-REIT484X-Project/config.json
# rsync --progress --recursive --delete --exclude-from=".rsyncignore" ./preprocessor.py jntwo@192.168.0.101:UQ-REIT484X-Project/preprocessor.py