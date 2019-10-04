DROP PROCEDURE IF EXISTS `writemac`;
DELIMITER ;;
CREATE DEFINER=`freeradius`@`%` PROCEDURE `writemac`(IN v_mac VARCHAR(12), IN v_datetime DATETIME)
BEGIN

	DECLARE mycheck INT DEFAULT 0;

	select count(*) into mycheck from macs_tmp where mac = v_mac;


	IF mycheck = 0 THEN

            INSERT INTO macs_tmp(mac, date_time) VALUES(v_mac, v_datetime);

	END IF;

END ;;
DELIMITER ;
