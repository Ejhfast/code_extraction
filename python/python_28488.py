# How do I define my model if I need an auto-incrementing ID but want to check for duplicates on another field?
ALTER TABLE `tablename` ADD UNIQUE INDEX `ttt_url` (`url`);
