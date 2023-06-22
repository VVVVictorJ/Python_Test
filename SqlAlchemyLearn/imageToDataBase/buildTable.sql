/*
    建表DDL
*/

-- test.testimage definition

CREATE TABLE `testimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_blob` mediumblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- test.errorprocesstablemessage definition

CREATE TABLE `errorprocesstablemessage` (
  `errorSystem` text,
  `errorName` text,
  `signDate` text,
  `errorHappenDate` text,
  `processBeginAndEndDate` text,
  `filledTableUser` text,
  `personInCharge` text,
  `downTime` text,
  `duringTimeOne` text,
  `EffectServiceTime` text,
  `duringTimeTwo` text,
  `phenomenonAndProcessAndReasonAndDiscribtion` text,
  `consumedBackUp` text,
  `errorProcessingStaff` text,
  `responsibility` text,
  `correctiveAction` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- test.address definition

CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `address_FK` (`user_id`),
  CONSTRAINT `address_FK` FOREIGN KEY (`user_id`) REFERENCES `py_test` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- test.py_test definition

CREATE TABLE `py_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;