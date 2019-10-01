DROP PROCEDURE IF EXISTS `writefreecanal`;
DELIMITER ;;
CREATE DEFINER=`freeradius`@`%` PROCEDURE `writefreecanal`(IN v_ip VARCHAR(15))
BEGIN

	DECLARE mycheck INT DEFAULT 0;

	select count(*) into mycheck from radfreecharge as rad where rad.ip = v_ip;


	IF mycheck = 0 THEN

            INSERT INTO radfreecharge(ip) VALUES(v_ip);

	END IF;

END ;;
DELIMITER ;
