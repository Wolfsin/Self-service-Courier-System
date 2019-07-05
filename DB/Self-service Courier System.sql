SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS  `Goods_Information`;
CREATE TABLE `Goods_Information` (
  `goods_id` int(11) NOT NULL AUTO_INCREMENT,
  `express_number` varchar(45) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `container_number` varchar(10) NOT NULL,
  `pick_up_code` varchar(6) NOT NULL,
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `Goods_Status`;
CREATE TABLE `Goods_Status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `express_number` varchar(45) NOT NULL,
  `is_send_msg` tinyint(1) NOT NULL DEFAULT '0',
  `is_pick_up` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `Operation_record`;
CREATE TABLE `Operation_record` (
  `operation_id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `operation` varchar(32) NOT NULL,
  `operation_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`operation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `User`;
CREATE TABLE `User` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(45) NOT NULL,
  `phonenumber` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`userid`,`username`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

