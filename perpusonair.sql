-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 19 Des 2018 pada 09.54
-- Versi Server: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpusonair`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `Nama` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `judul` longtext NOT NULL,
  `path` longtext NOT NULL,
  `ukuran` double NOT NULL,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`id`, `id_user`, `judul`, `path`, `ukuran`, `upload_date`) VALUES
(1, 1, '/', '/1', 0, '2018-12-17 17:43:42'),
(4, 1, '3', '/1/3.pdf', 2341, '2018-12-18 22:49:33'),
(6, 1, 'folder', '/1/folder', 0, '2018-12-17 17:43:23'),
(16, 1, 'MEKANISME', '/1/MEKANISME.pdf', 241580, '2018-12-18 02:04:40'),
(17, 2, '/', '/2', 0, '2018-12-19 05:46:13'),
(18, 3, '/', '/3', 0, '2018-12-18 02:39:56'),
(19, 4, '/', '/4', 0, '2018-12-18 02:39:46'),
(20, 1, 'asem', '/1/asem', 0, '2018-12-18 22:49:18'),
(21, 5, '/', '/5', 0, '2018-12-19 05:42:49'),
(22, 6, '/', '/6', 0, '2018-12-19 05:48:39'),
(23, 6, 'coba', '/6/coba', 0, '2018-12-19 05:48:53'),
(24, 6, 'MEKANISME', '/6/coba/MEKANISME.pdf', 241580, '2018-12-19 05:49:13');

-- --------------------------------------------------------

--
-- Struktur dari tabel `log`
--

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `id_admin` int(11) NOT NULL,
  `id_request` int(11) NOT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `requestmemory`
--

CREATE TABLE `requestmemory` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `request_memory` double NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `password` text NOT NULL,
  `memory` double NOT NULL,
  `root_id` int(11) NOT NULL,
  `tanggal_gabung` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `email`, `nama`, `password`, `memory`, `root_id`, `tanggal_gabung`) VALUES
(1, 'yoza@gmail.com', 'yoza', '1192749255', 5000000000, 1, '2018-12-18 02:21:28'),
(2, 'tayar@gmail.com', 'tayar', '1723328704', 1000000000, 17, '2018-12-19 05:46:25'),
(3, 'fajri@gmail.com', 'fajri', '1723328704', 1000000000, 18, '2018-12-19 05:46:28'),
(4, 'dio@gmail.com', 'dio', '1723328704', 1000000000, 19, '2018-12-19 05:46:31'),
(5, 'coba@gmail.com', 'coba', '1723328704', 1000000000, 21, '2018-12-19 05:46:35'),
(6, 'fuad@gmail.com', 'fuad', '1723328704', 1000000000, 22, '2018-12-19 05:48:39');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `requestmemory`
--
ALTER TABLE `requestmemory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
