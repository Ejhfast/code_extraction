# Django database - how to add this column in raw SQL
ALTER TABLE `appname_books` ADD COLUMN `user_id` INTEGER NOT NULL UNIQUE;
ALTER TABLE `appname_books` ADD CONSTRAINT `user_id_refs_user` FOREIGN KEY (`user_id`) REFERENCES auth_user (`id`);
