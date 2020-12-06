create database trasport

use trasport

CREATE TABLE IF NOT EXISTS `trasport`.`demanda` (
  `idDemanda` INT NOT NULL AUTO_INCREMENT,
  `precio` int,
  `mes` VARCHAR(20) NULL DEFAULT NULL,
  `demanda` int,
   PRIMARY KEY (`idDemanda`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

select * from demanda


DELETE FROM `trasport`.`demanda`
WHERE idDemanda >0;
