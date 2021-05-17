-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: PP_MiniProject
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basket`
--

DROP TABLE IF EXISTS `basket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basket` (
  `P_ID` varchar(25) DEFAULT NULL,
  `P_NAME` char(30) DEFAULT NULL,
  `P_PRICE` int DEFAULT NULL,
  `P_QUAN` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basket`
--

LOCK TABLES `basket` WRITE;
/*!40000 ALTER TABLE `basket` DISABLE KEYS */;
INSERT INTO `basket` VALUES ('ose01','Oxidised Silver Earrings',200,1),('fb02','Friends Bracelet',150,2);
/*!40000 ALTER TABLE `basket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `c_credit_debit`
--

DROP TABLE IF EXISTS `c_credit_debit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `c_credit_debit` (
  `C_NO` bigint DEFAULT NULL,
  `C_NAME` char(25) DEFAULT NULL,
  `C_CVV` int DEFAULT NULL,
  `C_VALIDTHRU` char(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `c_credit_debit`
--

LOCK TABLES `c_credit_debit` WRITE;
/*!40000 ALTER TABLE `c_credit_debit` DISABLE KEYS */;
INSERT INTO `c_credit_debit` VALUES (9876123456784321,'xyz',897,'12-22'),(547547,'hhdfh',564,'12-23');
/*!40000 ALTER TABLE `c_credit_debit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `C_UID` varchar(25) DEFAULT NULL,
  `C_NAME` char(25) DEFAULT NULL,
  `C_EMAIL` varchar(50) DEFAULT NULL,
  `C_PHONE` bigint DEFAULT NULL,
  `C_DOB` date DEFAULT NULL,
  `C_PASSWD` char(10) DEFAULT NULL,
  `C_ADDRESS` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('abhi.sharma','Abhishek Sharma','abhisharma04@gmail.com',9046894117,'2000-09-04','abhira2018','04 - Sharma Villa, Indira Nagar, Chandigarh');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `P_NAME` varchar(50) DEFAULT NULL,
  `P_PRICE` int DEFAULT NULL,
  `P_QUAN` int DEFAULT NULL,
  `P_DESC` varchar(300) DEFAULT NULL,
  `P_ID` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('Red Bandhani Saree',700,20,'A very delicate material with amazing red hues and black lace.','bandhsaree1'),('Banarasi Saree',1300,15,'Fabric - Banarasi Art Silk, Colour - Blue, Blouse - White with Blue Lace','banarassaree2'),('Oxidised Silver Earrings',200,29,'Gorgeous Heavy Look Ethnic Chandbali Hook Earrings in Silver Tone','ose01'),('Friends Bracelet',150,18,'Customizable Friends Bracelet with an Infinity Pattern and FRIENDS Logo','fb02'),('Shadow Hunters Pendant',180,25,'With Silver Colour Alloy Moon Pendant ShadowHunters Angelic Rune Necklace','shp03');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s_account`
--

DROP TABLE IF EXISTS `s_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s_account` (
  `S_BNAME` char(30) DEFAULT NULL,
  `S_BBRANCH` char(30) DEFAULT NULL,
  `S_BACCNAME` char(25) DEFAULT NULL,
  `S_BACCNO` bigint DEFAULT NULL,
  `S_IFSC` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s_account`
--

LOCK TABLES `s_account` WRITE;
/*!40000 ALTER TABLE `s_account` DISABLE KEYS */;
INSERT INTO `s_account` VALUES ('Bank of Baroda','Surat','Manish Patel',9876543212345678,'BARB0KIM'),('HDFC Bank','Calangut','Jasmine De Souza',1234567890123456,'HDFC00059');
/*!40000 ALTER TABLE `s_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `USERID` varchar(25) NOT NULL,
  `NAME` char(25) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `PHONE` bigint DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `PASSWD` char(10) DEFAULT NULL,
  `ADDRESS` varchar(100) DEFAULT NULL,
  `SOCIAL_MEDIA` char(20) DEFAULT NULL,
  PRIMARY KEY (`USERID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES ('jdesouza95','Jasmine De Souza','desouzaj95@yahoo.com',8975643120,'1995-11-05','cookie2001','09, De Souza Villa, Calangut, Goa','Instagram'),('manish1978','Manish Patel','manishp1978@gmail.com',9876543210,'1978-05-16','mpatel1978','15/02, Krishna Nivas, Surat','Facebook');
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-16 20:00:00
