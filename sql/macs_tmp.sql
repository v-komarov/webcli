DROP TABLE IF EXISTS `macs_tmp`;
CREATE TABLE `macs_tmp` (
   `mac` varchar(20) default '',
   `date_time` datetime default now()
);
