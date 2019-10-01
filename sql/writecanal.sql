DROP PROCEDURE IF EXISTS `writecanal`;
DELIMITER ;;
CREATE DEFINER=`freeradius`@`%` PROCEDURE `writecanal`(IN v_ip VARCHAR(15))
BEGIN

	DECLARE mycheck INT DEFAULT 0;
        DECLARE checkempty INT DEFAULT 0;
        DECLARE myid INT DEFAULT 0;

	SELECT count(*) INTO mycheck FROM radpackets AS rad WHERE rad.value = v_ip and pid=0;


	IF mycheck = 0 THEN
            
            SELECT count(*) INTO checkempty FROM radpackets AS rad;

            IF checkempty != 0 THEN
                   SELECT max(id) INTO myid FROM radpackets;
            END IF;

            INSERT INTO radpackets(id,pid,value) VALUES(myid+1,0,v_ip);

	END IF;

END ;;
DELIMITER ;
