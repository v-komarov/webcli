DROP TABLE IF EXISTS `user_logs`;
CREATE TABLE `user_logs` (
   `date_time` datetime default now(),
   `username` varchar(30) default '',
   `action` varchar(255) default ''
);
