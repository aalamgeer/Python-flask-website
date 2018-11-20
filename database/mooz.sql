-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2018 at 09:37 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mooz`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment_tbl`
--

CREATE TABLE `comment_tbl` (
  `id` int(11) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `created` datetime NOT NULL,
  `ip_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comment_tbl`
--

INSERT INTO `comment_tbl` (`id`, `comment`, `created`, `ip_address`) VALUES
(1, 'Your attitude and work level suits us here, so keep up the good work!', '2018-10-11 18:10:59', '127.0.0.1'),
(2, 'Thank you for giving me the chance to fulfill my potential here.', '2018-10-11 18:10:59', '127.0.0.1'),
(3, 'Hello,\r\nYou are doing well, Focus on spelling while code.\r\n\r\nThanks ', '2018-10-11 18:10:59', '127.0.0.1'),
(4, 'Php is no. 1 language in world. lol', '2018-10-13 11:08:04', '127.0.0.1'),
(5, 'Your support has made me a stronger person and I will forever be grateful.', '2018-10-13 11:09:24', '127.0.0.1');

-- --------------------------------------------------------

--
-- Table structure for table `contact_us`
--

CREATE TABLE `contact_us` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `mobile` tinyint(11) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `body` text NOT NULL,
  `created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact_us`
--

INSERT INTO `contact_us` (`id`, `name`, `email`, `mobile`, `subject`, `body`, `created`) VALUES
(1, 'Abhishek Agrawal', 'chita@myndsol.com', 127, 'Debugger', 'I have to arrogence', '0000-00-00 00:00:00'),
(2, 'AalamGeer Rana', 'aalamgeer@gmail.com', 127, 'Testing ', 'This is My blog for top ten articles.', '2018-10-11 14:45:56');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `Auther` varchar(50) NOT NULL,
  `post` text NOT NULL,
  `tags` varchar(50) NOT NULL,
  `created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `userId`, `title`, `Auther`, `post`, `tags`, `created`) VALUES
(1, 0, 'Top five programming languages now days.', 'AalamGeer Rana', 'Hello Dear folks,\r\n\r\nMy self Aalamgeer Rana Web developer.', 'Development', '0000-00-00 00:00:00'),
(2, 0, 'Second title text.', 'Abhishek Agrawal', 'Hello Dear folks,\r\n\r\nMy self Aalamgeer Rana Python & PHP developer.', 'Python', '0000-00-00 00:00:00'),
(3, 1, 'Bold Titles these', 'RANA G', 'Kuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahiKuch khas nahi', 'Hello sir', '2018-10-24 11:36:25');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `userEmail` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL,
  `address` varchar(250) NOT NULL,
  `avatar` varchar(25) NOT NULL,
  `updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `userName`, `userEmail`, `password`, `address`, `avatar`, `updated`, `created`) VALUES
(1, 'Aaalmgeer', 'aalamgeer10@myndsol.com', '12345678', 'Delhi', 'None', '2018-10-15 10:51:49', '2018-10-15 10:51:49'),
(2, 'Aaalmgeer', 'aalamgeer@myndsol.com', '12345678', 'Delhi', 'None', '2018-10-15 10:55:56', '2018-10-15 10:55:56'),
(3, 'Aaalmgeer', 'aalamgeer@myndsol.com', '12345678', 'Delhi', 'None', '2018-10-15 11:05:19', '2018-10-15 11:05:19'),
(4, 'Aaalmgeer', 'aalamgeer@myndsol.com', '12345678', 'Delhi', 'None', '2018-10-15 11:06:07', '2018-10-15 11:06:07'),
(5, 'abhishek', 'abhishek.agrawal@myndsol.', '1234', 'swswsw', 'None', '2018-10-15 11:33:35', '2018-10-15 11:33:35'),
(6, 'Aalageer', 'aalam@gmial.com', '123456', 'ASWET', 'None', '2018-10-15 11:37:04', '2018-10-15 11:37:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment_tbl`
--
ALTER TABLE `comment_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact_us`
--
ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment_tbl`
--
ALTER TABLE `comment_tbl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `contact_us`
--
ALTER TABLE `contact_us`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
