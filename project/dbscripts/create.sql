CREATE DATABASE  IF NOT EXISTS `shopping_cart`
/*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `shopping_cart`;

-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: shopping_cart
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `tot_price` decimal(18,2) NOT NULL,
  `tot_disc` decimal(18,2) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_item`
--

DROP TABLE IF EXISTS `cart_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_item` (
  `ci_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `p_id` int(11) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `cost` decimal(18,2) NOT NULL,
  PRIMARY KEY (`ci_id`),
  KEY `c_id` (`c_id`),
  KEY `p_id` (`p_id`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `cart` (`c_id`),
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `products` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_item`
--

LOCK TABLES `cart_item` WRITE;
/*!40000 ALTER TABLE `cart_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount_cart_amount`
--

DROP TABLE IF EXISTS `discount_cart_amount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount_cart_amount` (
  `dm_id` int(11) NOT NULL AUTO_INCREMENT,
  `min_amount` decimal(10,2) NOT NULL,
  `max_amount` decimal(10,2) NOT NULL,
  `disc_perc` decimal(10,2) DEFAULT NULL,
  `disc_amount` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`dm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_cart_amount`
--

LOCK TABLES `discount_cart_amount` WRITE;
/*!40000 ALTER TABLE `discount_cart_amount` DISABLE KEYS */;
INSERT INTO `discount_cart_amount` VALUES (1,50.00,100.00,5.00,NULL),(2,101.00,200.00,0.00,20.00);
/*!40000 ALTER TABLE `discount_cart_amount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount_multiples`
--

DROP TABLE IF EXISTS `discount_multiples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount_multiples` (
  `dm_id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` int(11) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `disc_perc` decimal(10,2) DEFAULT NULL,
  `disc_amount` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`dm_id`),
  KEY `p_id` (`p_id`),
  CONSTRAINT `discount_multiples_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `products` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_multiples`
--

LOCK TABLES `discount_multiples` WRITE;
/*!40000 ALTER TABLE `discount_multiples` DISABLE KEYS */;
INSERT INTO `discount_multiples` VALUES (1,1,3,5.00,NULL),(2,1,5,0.00,5.00);
/*!40000 ALTER TABLE `discount_multiples` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `price` decimal(18,2) NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'A',5.00),(2,'B',7.00),(3,'C',10.00),(4,'D',12.00),(5,'E',15.00);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-07 12:32:21
