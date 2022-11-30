-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         5.7.34 - MySQL Community Server (GPL)
-- SO del servidor:              Linux
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para rhdb_dev
CREATE DATABASE IF NOT EXISTS `rhdb_dev` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `rhdb_dev`;

-- Volcando estructura para tabla rhdb_dev.autenticacion_user
CREATE TABLE IF NOT EXISTS `autenticacion_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.autenticacion_user: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `autenticacion_user` DISABLE KEYS */;
INSERT INTO `autenticacion_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `image`) VALUES
	(1, 'pbkdf2_sha256$260000$zChegL9Py9mD5sYor5an6L$4VpnRU3Y8OzM6jebJ8ED5OurwJjDIuZucIHMMdSVxPQ=', '2022-11-23 22:00:53.589559', 1, 'lsomohano', 'Leonel', 'Somohano Carmona', 'lsomohano20@hotmail.com', 1, 1, '2022-10-07 17:35:44.000000', NULL, 'users/219983.png'),
	(2, 'pbkdf2_sha256$260000$kW5j5pJ1SAM09GvRfjvwzq$/DAvN9pqu3+0WRZBDzsOuAF2O+usbpj4+sGbozBB3kk=', '2022-11-29 15:14:44.000000', 0, 'lsomohano20', 'Proveedor', 'Veracruz', 'lsomohano20@gmail.com', 0, 1, '2022-10-07 17:54:59.000000', '985471245', 'users/img.jpg'),
	(3, 'pbkdf2_sha256$260000$lDnXtUM4SllivZapSyTpKw$xhcOm+1v9d4uG9yOcQU0izAMYVWdbAuwWC88mpdaUgc=', '2022-11-28 16:36:54.000000', 0, 'gerente.ver', 'Gerente', 'Veracruz', 'gveracruz@mail.com', 0, 1, '2022-10-13 21:25:08.000000', '741258963', 'users/img_dF0xm2b.jpg'),
	(4, 'pbkdf2_sha256$260000$DLbQdn3aMH9ScCkB32XwBQ$Zq8zybYXJn3AfhDGrmWcZdx5oeRLkD7b1hN4n4KliSI=', '2022-11-28 22:10:44.000000', 0, 'corporativo.rh', 'RH', 'Corporativo', 'corporativo@avasa.com.mx', 0, 1, '2022-11-28 22:03:40.000000', '748547842', 'users/QR.jpg');
/*!40000 ALTER TABLE `autenticacion_user` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.autenticacion_user_groups
CREATE TABLE IF NOT EXISTS `autenticacion_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `autenticacion_user_groups_user_id_group_id_b54467da_uniq` (`user_id`,`group_id`),
  KEY `autenticacion_user_groups_group_id_ae33056f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `autenticacion_user_g_user_id_8ed1f908_fk_autentica` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`),
  CONSTRAINT `autenticacion_user_groups_group_id_ae33056f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.autenticacion_user_groups: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `autenticacion_user_groups` DISABLE KEYS */;
INSERT INTO `autenticacion_user_groups` (`id`, `user_id`, `group_id`) VALUES
	(3, 2, 2),
	(1, 3, 1),
	(2, 4, 3);
/*!40000 ALTER TABLE `autenticacion_user_groups` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.autenticacion_user_user_permissions
CREATE TABLE IF NOT EXISTS `autenticacion_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `autenticacion_user_user__user_id_permission_id_5370839b_uniq` (`user_id`,`permission_id`),
  KEY `autenticacion_user_u_permission_id_6440ca10_fk_auth_perm` (`permission_id`),
  CONSTRAINT `autenticacion_user_u_permission_id_6440ca10_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `autenticacion_user_u_user_id_77611222_fk_autentica` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.autenticacion_user_user_permissions: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `autenticacion_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `autenticacion_user_user_permissions` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.auth_group: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` (`id`, `name`) VALUES
	(2, 'Proveedores'),
	(3, 'RH Admin'),
	(1, 'RH Gerentes');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.auth_group_permissions: ~86 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
	(87, 1, 32),
	(2, 1, 100),
	(1, 1, 101),
	(84, 1, 104),
	(85, 1, 108),
	(4, 2, 89),
	(90, 2, 90),
	(6, 2, 93),
	(7, 2, 94),
	(3, 2, 104),
	(8, 3, 21),
	(9, 3, 22),
	(10, 3, 23),
	(11, 3, 24),
	(12, 3, 25),
	(13, 3, 26),
	(14, 3, 27),
	(15, 3, 28),
	(16, 3, 29),
	(17, 3, 30),
	(18, 3, 31),
	(19, 3, 32),
	(20, 3, 33),
	(21, 3, 34),
	(22, 3, 35),
	(23, 3, 36),
	(24, 3, 37),
	(25, 3, 38),
	(26, 3, 39),
	(27, 3, 40),
	(28, 3, 41),
	(29, 3, 42),
	(30, 3, 43),
	(31, 3, 44),
	(32, 3, 45),
	(33, 3, 46),
	(34, 3, 47),
	(35, 3, 48),
	(36, 3, 49),
	(37, 3, 50),
	(38, 3, 51),
	(39, 3, 52),
	(40, 3, 53),
	(41, 3, 54),
	(42, 3, 55),
	(43, 3, 56),
	(44, 3, 57),
	(45, 3, 58),
	(46, 3, 59),
	(47, 3, 60),
	(48, 3, 61),
	(49, 3, 62),
	(50, 3, 63),
	(51, 3, 64),
	(52, 3, 77),
	(53, 3, 78),
	(54, 3, 79),
	(55, 3, 80),
	(56, 3, 85),
	(57, 3, 86),
	(58, 3, 87),
	(59, 3, 88),
	(60, 3, 89),
	(61, 3, 90),
	(62, 3, 91),
	(63, 3, 92),
	(64, 3, 93),
	(65, 3, 94),
	(66, 3, 95),
	(67, 3, 96),
	(68, 3, 101),
	(69, 3, 102),
	(70, 3, 103),
	(71, 3, 104),
	(72, 3, 105),
	(73, 3, 106),
	(74, 3, 107),
	(75, 3, 108),
	(76, 3, 109),
	(77, 3, 110),
	(78, 3, 111),
	(79, 3, 112),
	(80, 3, 113),
	(81, 3, 114),
	(82, 3, 115),
	(83, 3, 116);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.auth_permission: ~116 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add content type', 4, 'add_contenttype'),
	(14, 'Can change content type', 4, 'change_contenttype'),
	(15, 'Can delete content type', 4, 'delete_contenttype'),
	(16, 'Can view content type', 4, 'view_contenttype'),
	(17, 'Can add session', 5, 'add_session'),
	(18, 'Can change session', 5, 'change_session'),
	(19, 'Can delete session', 5, 'delete_session'),
	(20, 'Can view session', 5, 'view_session'),
	(21, 'Can add ciudad', 6, 'add_ciudades'),
	(22, 'Can change ciudad', 6, 'change_ciudades'),
	(23, 'Can delete ciudad', 6, 'delete_ciudades'),
	(24, 'Can view ciudad', 6, 'view_ciudades'),
	(25, 'Can add entidad', 7, 'add_entidades'),
	(26, 'Can change entidad', 7, 'change_entidades'),
	(27, 'Can delete entidad', 7, 'delete_entidades'),
	(28, 'Can view entidad', 7, 'view_entidades'),
	(29, 'Can add locacion', 8, 'add_locaciones'),
	(30, 'Can change locacion', 8, 'change_locaciones'),
	(31, 'Can delete locacion', 8, 'delete_locaciones'),
	(32, 'Can view locacion', 8, 'view_locaciones'),
	(33, 'Can add puesto', 9, 'add_puestosnominas'),
	(34, 'Can change puesto', 9, 'change_puestosnominas'),
	(35, 'Can delete puesto', 9, 'delete_puestosnominas'),
	(36, 'Can view puesto', 9, 'view_puestosnominas'),
	(37, 'Can add puesto operativo', 10, 'add_puestosoperativos'),
	(38, 'Can change puesto operativo', 10, 'change_puestosoperativos'),
	(39, 'Can delete puesto operativo', 10, 'delete_puestosoperativos'),
	(40, 'Can view puesto operativo', 10, 'view_puestosoperativos'),
	(41, 'Can add locacione puesto', 11, 'add_locacionespuestos'),
	(42, 'Can change locacione puesto', 11, 'change_locacionespuestos'),
	(43, 'Can delete locacione puesto', 11, 'delete_locacionespuestos'),
	(44, 'Can view locacione puesto', 11, 'view_locacionespuestos'),
	(45, 'Can add contacto', 12, 'add_contactos'),
	(46, 'Can change contacto', 12, 'change_contactos'),
	(47, 'Can delete contacto', 12, 'delete_contactos'),
	(48, 'Can view contacto', 12, 'view_contactos'),
	(49, 'Can add proveedor', 13, 'add_proveedores'),
	(50, 'Can change proveedor', 13, 'change_proveedores'),
	(51, 'Can delete proveedor', 13, 'delete_proveedores'),
	(52, 'Can view proveedor', 13, 'view_proveedores'),
	(53, 'Can add locacion proveedor', 14, 'add_locacionesproveedores'),
	(54, 'Can change locacion proveedor', 14, 'change_locacionesproveedores'),
	(55, 'Can delete locacion proveedor', 14, 'delete_locacionesproveedores'),
	(56, 'Can view locacion proveedor', 14, 'view_locacionesproveedores'),
	(57, 'Can add contacto proveedor', 15, 'add_contactosproveedores'),
	(58, 'Can change contacto proveedor', 15, 'change_contactosproveedores'),
	(59, 'Can delete contacto proveedor', 15, 'delete_contactosproveedores'),
	(60, 'Can view contacto proveedor', 15, 'view_contactosproveedores'),
	(61, 'Can add user', 16, 'add_user'),
	(62, 'Can change user', 16, 'change_user'),
	(63, 'Can delete user', 16, 'delete_user'),
	(64, 'Can view user', 16, 'view_user'),
	(65, 'Can add Site Tree', 17, 'add_tree'),
	(66, 'Can change Site Tree', 17, 'change_tree'),
	(67, 'Can delete Site Tree', 17, 'delete_tree'),
	(68, 'Can view Site Tree', 17, 'view_tree'),
	(69, 'Can add Site Tree Item', 18, 'add_treeitem'),
	(70, 'Can change Site Tree Item', 18, 'change_treeitem'),
	(71, 'Can delete Site Tree Item', 18, 'delete_treeitem'),
	(72, 'Can view Site Tree Item', 18, 'view_treeitem'),
	(73, 'Can add candidato estatus', 19, 'add_candidatosestatus'),
	(74, 'Can change candidato estatus', 19, 'change_candidatosestatus'),
	(75, 'Can delete candidato estatus', 19, 'delete_candidatosestatus'),
	(76, 'Can view candidato estatus', 19, 'view_candidatosestatus'),
	(77, 'Can add candidato documneto', 20, 'add_candidatosdocumentos'),
	(78, 'Can change candidato documneto', 20, 'change_candidatosdocumentos'),
	(79, 'Can delete candidato documneto', 20, 'delete_candidatosdocumentos'),
	(80, 'Can view candidato documneto', 20, 'view_candidatosdocumentos'),
	(81, 'Can add catalogo estatus', 21, 'add_estatus'),
	(82, 'Can change catalogo estatus', 21, 'change_estatus'),
	(83, 'Can delete catalogo estatus', 21, 'delete_estatus'),
	(84, 'Can view catalogo estatus', 21, 'view_estatus'),
	(85, 'Can add documento', 22, 'add_documentos'),
	(86, 'Can change documento', 22, 'change_documentos'),
	(87, 'Can delete documento', 22, 'delete_documentos'),
	(88, 'Can view documento', 22, 'view_documentos'),
	(89, 'Can add candidato', 23, 'add_candidatos'),
	(90, 'Can change candidato', 23, 'change_candidatos'),
	(91, 'Can delete candidato', 23, 'delete_candidatos'),
	(92, 'Can view candidato', 23, 'view_candidatos'),
	(93, 'Can add persona', 24, 'add_personas'),
	(94, 'Can change persona', 24, 'change_personas'),
	(95, 'Can delete persona', 24, 'delete_personas'),
	(96, 'Can view persona', 24, 'view_personas'),
	(97, 'Can add solicitud estatus', 25, 'add_solicitudesestatus'),
	(98, 'Can change solicitud estatus', 25, 'change_solicitudesestatus'),
	(99, 'Can delete solicitud estatus', 25, 'delete_solicitudesestatus'),
	(100, 'Can view solicitud estatus', 25, 'view_solicitudesestatus'),
	(101, 'Can add solicitud vacante', 26, 'add_solicitudesvacantes'),
	(102, 'Can change solicitud vacante', 26, 'change_solicitudesvacantes'),
	(103, 'Can delete solicitud vacante', 26, 'delete_solicitudesvacantes'),
	(104, 'Can view solicitud vacante', 26, 'view_solicitudesvacantes'),
	(105, 'Can add entrevista', 27, 'add_entrevistas'),
	(106, 'Can change entrevista', 27, 'change_entrevistas'),
	(107, 'Can delete entrevista', 27, 'delete_entrevistas'),
	(108, 'Can view entrevista', 27, 'view_entrevistas'),
	(109, 'Can add factura', 28, 'add_facturas'),
	(110, 'Can change factura', 28, 'change_facturas'),
	(111, 'Can delete factura', 28, 'delete_facturas'),
	(112, 'Can view factura', 28, 'view_facturas'),
	(113, 'Can add candidatos', 29, 'add_facturascandidatos'),
	(114, 'Can change candidatos', 29, 'change_facturascandidatos'),
	(115, 'Can delete candidatos', 29, 'delete_facturascandidatos'),
	(116, 'Can view candidatos', 29, 'view_facturascandidatos');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.calogos_estatus
CREATE TABLE IF NOT EXISTS `calogos_estatus` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estatus` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `activo` varchar(1) NOT NULL,
  `tipos` varchar(9) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.calogos_estatus: ~16 rows (aproximadamente)
/*!40000 ALTER TABLE `calogos_estatus` DISABLE KEYS */;
INSERT INTO `calogos_estatus` (`id`, `estatus`, `descripcion`, `activo`, `tipos`, `created`, `updated`) VALUES
	(1, 'Abierta', 'Cuando se crea y no tiene candidatos cargados. X', 'Y', 'solicitud', '2022-10-14 16:26:04.928690', '2022-10-14 16:26:04.928755'),
	(2, 'En proceso', 'Cuando se carga al primer candidato.', 'Y', 'solicitud', '2022-10-14 16:29:26.287719', '2022-10-14 16:29:26.287762'),
	(3, 'Cubierta', 'Cuando se cubrieron todas las vacantes de la solicitud', 'N', 'solicitud', '2022-10-14 18:38:28.773754', '2022-10-14 18:38:28.773782'),
	(4, 'En garantía', 'Cuando se contrata al candidato y esta en periodo garantía.', 'N', 'candidato', '2022-10-14 18:39:19.030780', '2022-10-14 18:39:19.030812'),
	(5, 'Facturado', 'Cuando el candidato cumple el periodo de garantía y se paga la factura.', 'N', 'solicitud', '2022-10-14 18:39:47.568093', '2022-10-14 18:39:47.568122'),
	(6, 'No cubierta', 'Cuando el proveedor no cumplió con el cubrimiento.', 'N', 'solicitud', '2022-10-14 18:40:13.850368', '2022-10-14 18:40:13.850395'),
	(7, 'No garantía', 'Cuando ya se utilizo la garantia correspondiente a la vacante a cubrir', 'N', 'solicitud', '2022-10-14 18:40:32.932262', '2022-10-14 18:40:32.932297'),
	(8, 'Postulado', 'El candidato a agregado al proceso', 'Y', 'candidato', '2022-10-21 17:21:01.319993', '2022-10-21 17:21:01.320025'),
	(9, 'Programado', 'El candidato fue programado para entrevista', 'Y', 'candidato', '2022-10-21 17:22:13.267249', '2022-10-21 17:22:13.267283'),
	(10, 'Entrevistado', 'El candidato fue entrevistado', 'Y', 'candidato', '2022-10-21 17:23:12.487657', '2022-10-21 17:23:12.487691'),
	(11, 'Aceptado', 'El candidato fue aceptado para cubrir la posición', 'Y', 'candidato', '2022-11-07 20:59:51.953431', '2022-11-07 20:59:51.953467'),
	(12, 'Rechazado', 'El candidato fue rechazado del proceso.', 'Y', 'candidato', '2022-11-07 21:00:52.199968', '2022-11-07 21:00:52.200002'),
	(13, 'Contratación', 'El candidato esta en proceso de contratación', 'Y', 'candidato', '2022-11-07 21:01:46.241432', '2022-11-07 21:01:46.241468'),
	(14, 'Contratado', 'El candidato fue contratado.', 'Y', 'candidato', '2022-11-07 21:02:52.563479', '2022-11-07 21:02:52.563510'),
	(15, 'Facturación', 'El candidato fue ingresado a un reporte de facturación.', 'Y', 'candidato', '2022-11-07 21:05:06.183314', '2022-11-17 14:25:07.527059'),
	(16, 'Facturado', 'El proveedor ingreso una factura al proceso de facturación don de fue agregado el candidato.', 'Y', 'candidato', '2022-11-17 14:22:02.953355', '2022-11-17 14:23:17.771093');
/*!40000 ALTER TABLE `calogos_estatus` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.candidatos
CREATE TABLE IF NOT EXISTS `candidatos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reporte_entrevista` varchar(100) DEFAULT NULL,
  `evaluacion_psicometrica` varchar(100) DEFAULT NULL,
  `aceptado` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `personas_id` bigint(20) NOT NULL,
  `solicitudes_vacantes_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `cv_solicitud` varchar(100) DEFAULT NULL,
  `referencias` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `candidatos_personas_id_fb5da2ac_fk_personas_id` (`personas_id`),
  KEY `candidatos_solicitudes_vacantes_792afa3a_fk_solicitud` (`solicitudes_vacantes_id`),
  KEY `candidatos_user_id_d2e3a668_fk_autenticacion_user_id` (`user_id`),
  CONSTRAINT `candidatos_personas_id_fb5da2ac_fk_personas_id` FOREIGN KEY (`personas_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `candidatos_solicitudes_vacantes_792afa3a_fk_solicitud` FOREIGN KEY (`solicitudes_vacantes_id`) REFERENCES `solicitudes_vacantes` (`id`),
  CONSTRAINT `candidatos_user_id_d2e3a668_fk_autenticacion_user_id` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.candidatos: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `candidatos` DISABLE KEYS */;
INSERT INTO `candidatos` (`id`, `reporte_entrevista`, `evaluacion_psicometrica`, `aceptado`, `created`, `personas_id`, `solicitudes_vacantes_id`, `user_id`, `cv_solicitud`, `referencias`) VALUES
	(1, 'candidatos/personas/2__FDe3NEi.pdf', 'candidatos/personas/1__m3ZnRWe.pdf', 'Y', '2022-11-01 16:02:12.254130', 1, 1, 1, 'candidatos/personas/cv/3__z7kU5rZ.pdf', 'candidatos/referencias/3_.pdf'),
	(2, 'candidatos/personas/2__9s1BSuj.pdf', 'candidatos/personas/1__Tcc1dOp.pdf', 'Y', '2022-11-09 23:26:22.466820', 2, 1, 1, 'candidatos/personas/cv/carta.pdf', 'candidatos/referencias/3__rG6oUSF.pdf'),
	(3, 'candidatos/personas/3__uchQv8v.pdf', 'candidatos/personas/1__CBBx7DE.pdf', 'Y', '2022-11-09 23:27:57.427084', 3, 1, 1, 'candidatos/personas/cv/2_.pdf', 'candidatos/referencias/carta.pdf'),
	(4, 'candidatos/personas/3__ZZCPDjo.pdf', 'candidatos/personas/2__ZpKFAQx.pdf', 'Y', '2022-11-20 00:34:27.464960', 4, 1, 1, 'candidatos/personas/cv/1__EmNBpXq.pdf', 'candidatos/referencias/carta_JACbvH7.pdf'),
	(5, 'candidatos/personas/3__is9Sg0b.pdf', 'candidatos/personas/2__fK2H3V4.pdf', 'Y', '2022-11-23 22:29:51.349844', 5, 2, 1, 'candidatos/personas/cv/1__YijSJkb.pdf', 'candidatos/referencias/carta_9vNlDqe.pdf'),
	(6, 'candidatos/personas/2__Gx52ImX.pdf', 'candidatos/personas/3__El0ILAR.pdf', 'Y', '2022-11-23 22:18:07.043417', 6, 4, 1, 'candidatos/personas/cv/1__Hx4Em0c.pdf', 'candidatos/referencias/carta_sCJBOl1.pdf'),
	(7, 'candidatos/personas/3__i33fCeN.pdf', 'candidatos/personas/carta.pdf', 'Y', '2022-11-29 18:31:52.622400', 7, 1, 1, 'candidatos/personas/cv/1__ud3ryLQ.pdf', 'candidatos/referencias/3__saAghO1.pdf');
/*!40000 ALTER TABLE `candidatos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.candidatos_documentos
CREATE TABLE IF NOT EXISTS `candidatos_documentos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `check_proveedor` varchar(1) DEFAULT NULL,
  `check_locacion` varchar(1) DEFAULT NULL,
  `candidatos_id` bigint(20) NOT NULL,
  `documentos_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `candidatos_documentos_candidatos_id_14bb9dec_fk_candidatos_id` (`candidatos_id`),
  KEY `candidatos_documentos_documentos_id_6a740004_fk_documentos_id` (`documentos_id`),
  CONSTRAINT `candidatos_documentos_candidatos_id_14bb9dec_fk_candidatos_id` FOREIGN KEY (`candidatos_id`) REFERENCES `candidatos` (`id`),
  CONSTRAINT `candidatos_documentos_documentos_id_6a740004_fk_documentos_id` FOREIGN KEY (`documentos_id`) REFERENCES `documentos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.candidatos_documentos: ~90 rows (aproximadamente)
/*!40000 ALTER TABLE `candidatos_documentos` DISABLE KEYS */;
INSERT INTO `candidatos_documentos` (`id`, `check_proveedor`, `check_locacion`, `candidatos_id`, `documentos_id`) VALUES
	(1, 'Y', 'Y', 1, 1),
	(2, 'Y', 'Y', 1, 2),
	(3, 'Y', 'Y', 1, 3),
	(4, 'Y', 'Y', 1, 4),
	(5, 'Y', 'Y', 1, 5),
	(6, 'Y', 'Y', 1, 8),
	(7, 'Y', 'Y', 1, 9),
	(8, 'Y', 'Y', 1, 10),
	(9, 'Y', 'Y', 1, 11),
	(10, 'Y', 'Y', 1, 12),
	(11, 'Y', 'Y', 1, 13),
	(12, 'Y', 'Y', 1, 14),
	(13, 'Y', 'Y', 1, 15),
	(14, 'Y', 'Y', 1, 16),
	(15, 'N', 'Y', 1, 6),
	(16, 'N', 'Y', 1, 17),
	(17, 'Y', 'Y', 3, 1),
	(18, 'Y', 'Y', 3, 2),
	(19, 'Y', 'Y', 3, 3),
	(20, 'Y', 'Y', 3, 4),
	(21, 'Y', 'Y', 3, 5),
	(22, 'Y', 'Y', 3, 8),
	(23, 'Y', 'Y', 3, 9),
	(24, 'Y', 'Y', 3, 10),
	(25, 'Y', 'Y', 3, 11),
	(26, 'Y', 'Y', 3, 12),
	(27, 'Y', 'Y', 3, 13),
	(28, 'Y', 'Y', 3, 14),
	(29, 'Y', 'Y', 3, 15),
	(30, 'Y', 'Y', 3, 16),
	(31, 'N', 'Y', 3, 17),
	(32, 'Y', 'Y', 4, 1),
	(33, 'Y', 'Y', 4, 2),
	(34, 'Y', 'Y', 4, 3),
	(35, 'Y', 'Y', 4, 4),
	(36, 'Y', 'Y', 4, 5),
	(37, 'Y', 'Y', 4, 8),
	(38, 'Y', 'Y', 4, 9),
	(39, 'Y', 'Y', 4, 10),
	(40, 'Y', 'Y', 4, 11),
	(41, 'Y', 'Y', 4, 12),
	(42, 'Y', 'Y', 4, 13),
	(43, 'Y', 'Y', 4, 14),
	(44, 'Y', 'Y', 4, 15),
	(45, 'Y', 'Y', 4, 16),
	(46, 'Y', 'Y', 5, 1),
	(47, 'Y', 'Y', 5, 2),
	(48, 'Y', 'Y', 5, 3),
	(49, 'Y', 'Y', 5, 4),
	(50, 'Y', 'Y', 5, 5),
	(51, 'Y', 'Y', 5, 8),
	(52, 'Y', 'Y', 5, 9),
	(53, 'Y', 'Y', 5, 10),
	(54, 'Y', 'Y', 5, 11),
	(55, 'Y', 'Y', 5, 12),
	(56, 'Y', 'Y', 5, 13),
	(57, 'Y', 'Y', 5, 14),
	(58, 'Y', 'Y', 5, 15),
	(59, 'Y', 'Y', 5, 16),
	(60, 'N', 'Y', 4, 17),
	(61, 'Y', 'Y', 6, 1),
	(62, 'Y', 'Y', 6, 2),
	(63, 'Y', 'Y', 6, 3),
	(64, 'Y', 'Y', 6, 4),
	(65, 'Y', 'Y', 6, 5),
	(66, 'Y', 'Y', 6, 8),
	(67, 'Y', 'Y', 6, 9),
	(68, 'Y', 'Y', 6, 10),
	(69, 'Y', 'Y', 6, 11),
	(70, 'Y', 'Y', 6, 12),
	(71, 'Y', 'Y', 6, 13),
	(72, 'Y', 'Y', 6, 14),
	(73, 'Y', 'Y', 6, 15),
	(74, 'Y', 'Y', 6, 16),
	(75, 'N', 'Y', 6, 6),
	(76, 'N', 'Y', 6, 17),
	(77, 'Y', 'Y', 7, 1),
	(78, 'Y', 'Y', 7, 2),
	(79, 'Y', 'Y', 7, 3),
	(80, 'Y', 'Y', 7, 4),
	(81, 'Y', 'Y', 7, 5),
	(82, 'Y', 'Y', 7, 8),
	(83, 'Y', 'Y', 7, 9),
	(84, 'Y', 'Y', 7, 10),
	(85, 'Y', 'Y', 7, 11),
	(86, 'Y', 'Y', 7, 12),
	(87, 'Y', 'Y', 7, 13),
	(88, 'Y', 'Y', 7, 14),
	(89, 'Y', 'Y', 7, 15),
	(90, 'Y', 'Y', 7, 16);
/*!40000 ALTER TABLE `candidatos_documentos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.candidatos_estatus
CREATE TABLE IF NOT EXISTS `candidatos_estatus` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `candidatos_id` bigint(20) NOT NULL,
  `estatus_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `candidatos_estatus_candidatos_id_bc6832ac_fk_candidatos_id` (`candidatos_id`),
  KEY `candidatos_estatus_estatus_id_c4dbeaf3_fk_calogos_estatus_id` (`estatus_id`),
  CONSTRAINT `candidatos_estatus_candidatos_id_bc6832ac_fk_candidatos_id` FOREIGN KEY (`candidatos_id`) REFERENCES `candidatos` (`id`),
  CONSTRAINT `candidatos_estatus_estatus_id_c4dbeaf3_fk_calogos_estatus_id` FOREIGN KEY (`estatus_id`) REFERENCES `calogos_estatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.candidatos_estatus: ~43 rows (aproximadamente)
/*!40000 ALTER TABLE `candidatos_estatus` DISABLE KEYS */;
INSERT INTO `candidatos_estatus` (`id`, `activo`, `created`, `updated`, `candidatos_id`, `estatus_id`) VALUES
	(1, 'N', '2022-11-01 16:02:12.258358', '2022-11-01 16:02:12.258389', 1, 8),
	(2, 'N', '2022-11-03 12:37:08.000000', '2022-11-03 12:37:09.000000', 1, 9),
	(3, 'N', '2022-11-08 21:19:34.025104', '2022-11-08 21:19:34.025135', 1, 8),
	(4, 'N', '2022-11-08 21:27:26.425652', '2022-11-08 21:27:26.425714', 1, 10),
	(5, 'N', '2022-11-08 21:54:35.282959', '2022-11-08 21:54:35.282991', 1, 10),
	(6, 'N', '2022-11-09 16:10:17.746718', '2022-11-09 16:10:17.746748', 1, 10),
	(7, 'N', '2022-11-09 22:40:19.269988', '2022-11-09 22:40:19.270021', 1, 10),
	(8, 'N', '2022-11-09 23:03:39.738592', '2022-11-09 23:03:39.738624', 1, 10),
	(9, 'N', '2022-11-09 23:27:57.430723', '2022-11-09 23:27:57.430757', 3, 8),
	(10, 'N', '2022-11-14 16:57:15.729488', '2022-11-14 16:57:15.729677', 3, 10),
	(11, 'N', '2022-11-14 17:05:36.159634', '2022-11-14 17:05:36.159666', 3, 10),
	(12, 'N', '2022-11-14 17:11:21.172910', '2022-11-14 17:11:21.172942', 4, 8),
	(13, 'N', '2022-11-14 17:34:12.194683', '2022-11-14 17:34:12.194712', 4, 9),
	(14, 'N', '2022-11-15 15:47:54.963402', '2022-11-15 15:47:54.963433', 5, 8),
	(15, 'N', '2022-11-15 15:48:41.348173', '2022-11-15 15:48:41.348200', 5, 9),
	(16, 'N', '2022-11-15 16:06:08.261614', '2022-11-15 16:06:08.261645', 1, 13),
	(17, 'N', '2022-11-15 16:20:40.864004', '2022-11-15 16:20:40.864034', 3, 10),
	(18, 'N', '2022-11-15 17:40:12.737155', '2022-11-15 17:40:12.737191', 1, 14),
	(19, 'N', '2022-11-18 19:17:34.368750', '2022-11-18 19:17:34.370493', 3, 13),
	(20, 'N', '2022-11-18 19:17:55.521333', '2022-11-18 19:17:55.522596', 3, 14),
	(21, 'N', '2022-11-18 21:10:03.181807', '2022-11-18 21:10:03.183374', 4, 8),
	(22, 'N', '2022-11-19 17:48:11.873358', '2022-11-19 17:48:11.876569', 1, 15),
	(23, 'N', '2022-11-19 17:48:11.884831', '2022-11-19 17:48:11.886801', 3, 15),
	(24, 'N', '2022-11-20 00:34:14.718868', '2022-11-20 00:34:14.720617', 4, 9),
	(25, 'N', '2022-11-20 00:34:27.570860', '2022-11-20 00:34:27.572456', 4, 10),
	(26, 'N', '2022-11-20 00:34:47.699741', '2022-11-20 00:34:47.701386', 4, 13),
	(27, 'N', '2022-11-20 00:35:08.064287', '2022-11-20 00:35:08.066383', 4, 14),
	(28, 'Y', '2022-11-20 00:35:22.299207', '2022-11-20 00:35:22.300993', 4, 15),
	(29, 'Y', '2022-11-21 17:07:11.865509', '2022-11-21 17:07:11.868016', 1, 16),
	(30, 'Y', '2022-11-21 17:07:11.872854', '2022-11-21 17:07:11.874386', 3, 16),
	(31, 'N', '2022-11-23 22:05:53.540300', '2022-11-23 22:05:53.542509', 6, 8),
	(32, 'N', '2022-11-23 22:13:54.058715', '2022-11-23 22:13:54.060395', 6, 9),
	(33, 'N', '2022-11-23 22:18:07.145254', '2022-11-23 22:18:07.146485', 6, 10),
	(34, 'N', '2022-11-23 22:20:03.741058', '2022-11-23 22:20:03.743044', 6, 13),
	(35, 'N', '2022-11-23 22:20:53.920345', '2022-11-23 22:20:53.921820', 6, 14),
	(36, 'N', '2022-11-23 22:29:51.434817', '2022-11-23 22:29:51.436043', 5, 10),
	(37, 'N', '2022-11-23 22:30:29.766266', '2022-11-23 22:30:29.767539', 5, 13),
	(38, 'N', '2022-11-23 22:33:56.965042', '2022-11-23 22:33:56.966611', 5, 14),
	(39, 'N', '2022-11-23 22:53:43.120916', '2022-11-23 22:53:43.122634', 5, 15),
	(40, 'N', '2022-11-23 22:53:43.136631', '2022-11-23 22:53:43.138195', 6, 15),
	(41, 'Y', '2022-11-23 22:55:42.624071', '2022-11-23 22:55:42.625381', 5, 16),
	(42, 'Y', '2022-11-23 22:55:42.629778', '2022-11-23 22:55:42.631026', 6, 16),
	(43, 'N', '2022-11-28 15:49:27.467734', '2022-11-28 15:49:27.470373', 7, 8),
	(44, 'N', '2022-11-29 18:14:58.938480', '2022-11-29 18:14:58.945076', 7, 9),
	(45, 'N', '2022-11-29 18:31:52.725184', '2022-11-29 18:31:52.727187', 7, 10),
	(46, 'N', '2022-11-29 20:37:19.992937', '2022-11-29 20:37:19.994798', 7, 13),
	(47, 'Y', '2022-11-29 22:00:58.944594', '2022-11-29 22:00:58.947409', 7, 14);
/*!40000 ALTER TABLE `candidatos_estatus` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.ciudades
CREATE TABLE IF NOT EXISTS `ciudades` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(50) NOT NULL,
  `activo` varchar(5) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `entidades_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ciudades_entidades_id_3fda99ad_fk_entidades_id` (`entidades_id`),
  CONSTRAINT `ciudades_entidades_id_3fda99ad_fk_entidades_id` FOREIGN KEY (`entidades_id`) REFERENCES `entidades` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.ciudades: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` (`id`, `ciudad`, `activo`, `created`, `updated`, `entidades_id`) VALUES
	(1, 'Cancún', 'Y', '2022-10-07 23:18:51.063139', '2022-10-07 23:18:51.063177', 1),
	(2, 'Playa del Carmen', 'Y', '2022-10-07 23:19:01.866861', '2022-10-07 23:19:01.866898', 1),
	(3, 'Veracruz', 'Y', '2022-10-07 23:19:07.770962', '2022-10-07 23:19:07.770993', 2);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.contactos
CREATE TABLE IF NOT EXISTS `contactos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `horario_inicio` time(6) NOT NULL,
  `horario_termino` time(6) NOT NULL,
  `dias_atencion` varchar(50) NOT NULL,
  `activo` varchar(5) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `locaciones_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contactos_locaciones_id_d2996a72_fk_locaciones_id` (`locaciones_id`),
  KEY `contactos_user_id_794f8cc6` (`user_id`),
  CONSTRAINT `contactos_locaciones_id_d2996a72_fk_locaciones_id` FOREIGN KEY (`locaciones_id`) REFERENCES `locaciones` (`id`),
  CONSTRAINT `contactos_user_id_794f8cc6_fk_autenticacion_user_id` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.contactos: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `contactos` DISABLE KEYS */;
INSERT INTO `contactos` (`id`, `horario_inicio`, `horario_termino`, `dias_atencion`, `activo`, `created`, `updated`, `locaciones_id`, `user_id`) VALUES
	(1, '09:00:00.000000', '18:00:00.000000', 'LUN,MAR,MIE,JUE,VIE', 'Y', '2022-10-07 23:20:50.660747', '2022-10-07 23:20:50.660776', 1, 2),
	(2, '09:00:00.000000', '20:00:00.000000', 'LUN,MAR,MIE,JUE,VIE', 'Y', '2022-10-13 21:26:15.041726', '2022-10-13 21:26:15.041752', 2, 3);
/*!40000 ALTER TABLE `contactos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.contactos_proveedores
CREATE TABLE IF NOT EXISTS `contactos_proveedores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tipo_contacto` varchar(1) NOT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `proveedores_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contactos_proveedores_user_id_11e97a89_uniq` (`user_id`),
  KEY `contactos_proveedores_proveedores_id_961ac1ae_fk_proveedores_id` (`proveedores_id`),
  CONSTRAINT `contactos_proveedores_proveedores_id_961ac1ae_fk_proveedores_id` FOREIGN KEY (`proveedores_id`) REFERENCES `proveedores` (`id`),
  CONSTRAINT `contactos_proveedores_user_id_11e97a89_fk_autenticacion_user_id` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.contactos_proveedores: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `contactos_proveedores` DISABLE KEYS */;
INSERT INTO `contactos_proveedores` (`id`, `tipo_contacto`, `activo`, `created`, `updated`, `proveedores_id`, `user_id`) VALUES
	(1, 'P', 'Y', '2022-11-09 15:45:35.246359', '2022-11-09 15:45:35.246398', 1, 1);
/*!40000 ALTER TABLE `contactos_proveedores` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_autenticacion_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_autenticacion_user_id` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.django_admin_log: ~120 rows (aproximadamente)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2022-10-07 17:54:59.422622', '2', 'lsomohano20', 1, '[{"added": {}}]', 16, 1),
	(2, '2022-10-07 17:56:17.787289', '2', 'lsomohano20@gmail.com', 2, '[{"changed": {"fields": ["Username", "First name", "Last name", "Email address", "Last login"]}}]', 16, 1),
	(3, '2022-10-07 18:19:23.252835', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["Username"]}}]', 16, 1),
	(4, '2022-10-07 21:55:59.997999', '1', 'Gerentes', 1, '[{"added": {}}]', 3, 1),
	(5, '2022-10-07 22:06:42.909414', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["First name"]}}]', 16, 1),
	(6, '2022-10-07 22:26:27.611919', '1', 'lsomohano', 2, '[{"changed": {"fields": ["Image"]}}]', 16, 1),
	(7, '2022-10-07 23:02:11.379407', '1', 'AvasaRH', 1, '[{"added": {}}]', 17, 1),
	(8, '2022-10-07 23:02:38.136554', '1', 'Dashboard', 1, '[{"added": {}}]', 18, 1),
	(9, '2022-10-07 23:03:18.715507', '2', 'Proveedores', 1, '[{"added": {}}]', 18, 1),
	(10, '2022-10-07 23:03:43.642928', '3', 'Configuraciones', 1, '[{"added": {}}]', 18, 1),
	(11, '2022-10-07 23:04:25.782243', '4', 'Entidades', 1, '[{"added": {}}]', 18, 1),
	(12, '2022-10-07 23:04:58.074150', '5', 'Ciudades', 1, '[{"added": {}}]', 18, 1),
	(13, '2022-10-07 23:05:24.048843', '6', 'Locaciones', 1, '[{"added": {}}]', 18, 1),
	(14, '2022-10-07 23:05:43.936580', '7', 'Puestos', 1, '[{"added": {}}]', 18, 1),
	(15, '2022-10-07 23:06:04.796178', '1', 'Dashboard', 2, '[{"changed": {"fields": ["URL", "URL as Pattern"]}}]', 18, 1),
	(16, '2022-10-11 16:46:32.061687', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["Phone", "Image"]}}]', 16, 1),
	(17, '2022-10-11 18:18:11.529641', '8', 'Reclutamiento', 1, '[{"added": {}}]', 18, 1),
	(18, '2022-10-11 18:18:41.258477', '9', 'Solicitudes', 1, '[{"added": {}}]', 18, 1),
	(19, '2022-10-11 18:19:00.371236', '1', 'AvasaRH', 2, '[]', 17, 1),
	(20, '2022-10-13 15:01:53.986579', '2', 'VER50', 1, '[{"added": {}}]', 8, 1),
	(21, '2022-10-13 21:25:08.179536', '3', 'gerente.ver', 1, '[{"added": {}}]', 16, 1),
	(22, '2022-10-13 21:25:45.527541', '3', 'gerente.ver', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Phone", "Image"]}}]', 16, 1),
	(23, '2022-10-14 16:11:39.268074', '10', 'Catalogo Estatus', 1, '[{"added": {}}]', 18, 1),
	(24, '2022-10-14 18:38:28.777509', '3', 'Cubierta', 1, '[{"added": {}}]', 21, 1),
	(25, '2022-10-14 18:39:19.032453', '4', 'En garantía', 1, '[{"added": {}}]', 21, 1),
	(26, '2022-10-14 18:39:47.569842', '5', 'Facturado', 1, '[{"added": {}}]', 21, 1),
	(27, '2022-10-14 18:40:13.851963', '6', 'No cubierta', 1, '[{"added": {}}]', 21, 1),
	(28, '2022-10-14 18:40:32.934229', '7', 'No garantía', 1, '[{"added": {}}]', 21, 1),
	(29, '2022-10-14 18:45:06.408751', '10', 'Catalogo Estatus', 3, '', 18, 1),
	(30, '2022-10-17 21:22:48.704820', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["password"]}}]', 16, 1),
	(31, '2022-10-21 17:21:01.321590', '8', 'En porceso', 1, '[{"added": {}}]', 21, 1),
	(32, '2022-10-21 17:22:13.268106', '9', 'En entrevista', 1, '[{"added": {}}]', 21, 1),
	(33, '2022-10-21 17:22:31.882300', '9', 'Agendado', 2, '[{"changed": {"fields": ["Estatus", "Tipos"]}}]', 21, 1),
	(34, '2022-10-21 17:23:12.488479', '10', 'Entrevistado', 1, '[{"added": {}}]', 21, 1),
	(35, '2022-10-28 21:48:12.646860', '1', 'Acta de nacimiento', 1, '[{"added": {}}]', 22, 1),
	(36, '2022-10-28 21:48:33.483249', '2', 'Credencial de elector', 1, '[{"added": {}}]', 22, 1),
	(37, '2022-10-28 21:48:45.181117', '3', 'CURP', 1, '[{"added": {}}]', 22, 1),
	(38, '2022-10-28 21:49:13.999263', '4', 'Numero de seguro social', 1, '[{"added": {}}]', 22, 1),
	(39, '2022-10-28 21:50:17.172110', '5', 'Comprobante de Domicilio', 1, '[{"added": {}}]', 22, 1),
	(40, '2022-10-28 21:50:42.585096', '4', 'Numero de seguro social', 2, '[{"changed": {"fields": ["Descripcion"]}}]', 22, 1),
	(41, '2022-10-28 21:51:21.589924', '6', 'Aviso de retenciones Infonavit', 1, '[{"added": {}}]', 22, 1),
	(42, '2022-10-28 21:52:07.023339', '7', 'Estado de cuenta FONACOT', 1, '[{"added": {}}]', 22, 1),
	(43, '2022-10-28 21:53:30.653527', '8', 'RFC', 1, '[{"added": {}}]', 22, 1),
	(44, '2022-10-28 21:54:12.647318', '9', 'Curriculum Vitae', 1, '[{"added": {}}]', 22, 1),
	(45, '2022-10-28 21:54:35.347282', '10', 'Solicitud de empleo', 1, '[{"added": {}}]', 22, 1),
	(46, '2022-10-28 21:54:53.959393', '11', 'Licencia de conducir', 1, '[{"added": {}}]', 22, 1),
	(47, '2022-10-28 21:55:12.294235', '12', 'Cartilla militar', 1, '[{"added": {}}]', 22, 1),
	(48, '2022-10-28 21:55:48.334016', '13', 'Comprobante de estudios', 1, '[{"added": {}}]', 22, 1),
	(49, '2022-10-28 21:56:25.666091', '14', 'Constancias laborales', 1, '[{"added": {}}]', 22, 1),
	(50, '2022-10-28 21:56:43.116706', '15', 'Afore', 1, '[{"added": {}}]', 22, 1),
	(51, '2022-10-28 21:57:09.685141', '16', 'Antecedentes no penales', 1, '[{"added": {}}]', 22, 1),
	(52, '2022-10-28 21:57:43.172683', '17', 'Fotos tamaño infantil', 1, '[{"added": {}}]', 22, 1),
	(53, '2022-10-28 21:57:58.074122', '2', 'Credencial de elector', 2, '[{"changed": {"fields": ["Descripcion"]}}]', 22, 1),
	(54, '2022-10-28 21:58:41.156586', '1', 'Acta de nacimiento', 2, '[{"changed": {"fields": ["Descripcion"]}}]', 22, 1),
	(55, '2022-10-31 15:00:48.565331', '7', 'Estado de cuenta FONACOT', 2, '[{"changed": {"fields": ["Consideraciones"]}}]', 22, 1),
	(56, '2022-10-31 15:01:01.204642', '6', 'Aviso de retenciones Infonavit', 2, '[{"changed": {"fields": ["Consideraciones"]}}]', 22, 1),
	(57, '2022-10-31 15:01:27.938360', '17', 'Fotos tamaño infantil', 2, '[{"changed": {"fields": ["Consideraciones"]}}]', 22, 1),
	(58, '2022-11-03 18:07:41.064997', '10', 'Entrevistas', 1, '[{"added": {}}]', 18, 1),
	(59, '2022-11-07 17:02:34.448278', '9', 'Programado', 2, '[{"changed": {"fields": ["Estatus"]}}]', 21, 1),
	(60, '2022-11-07 20:57:45.197350', '8', 'Postulado', 2, '[{"changed": {"fields": ["Estatus"]}}]', 21, 1),
	(61, '2022-11-07 20:59:51.954983', '11', 'Aceptado', 1, '[{"added": {}}]', 21, 1),
	(62, '2022-11-07 21:00:52.201343', '12', 'Rechazado', 1, '[{"added": {}}]', 21, 1),
	(63, '2022-11-07 21:01:46.242822', '13', 'Contratación', 1, '[{"added": {}}]', 21, 1),
	(64, '2022-11-07 21:02:52.564663', '14', 'Contratado', 1, '[{"added": {}}]', 21, 1),
	(65, '2022-11-07 21:05:06.184485', '15', 'Facturado', 1, '[{"added": {}}]', 21, 1),
	(66, '2022-11-07 21:05:28.215507', '7', 'No garantía', 2, '[{"changed": {"fields": ["Activo"]}}]', 21, 1),
	(67, '2022-11-07 21:05:39.254247', '6', 'No cubierta', 2, '[{"changed": {"fields": ["Activo"]}}]', 21, 1),
	(68, '2022-11-07 21:05:48.216259', '5', 'Facturado', 2, '[{"changed": {"fields": ["Activo"]}}]', 21, 1),
	(69, '2022-11-07 21:05:59.025282', '4', 'En garantía', 2, '[{"changed": {"fields": ["Tipos"]}}]', 21, 1),
	(70, '2022-11-07 21:06:15.533422', '4', 'En garantía', 2, '[{"changed": {"fields": ["Activo"]}}]', 21, 1),
	(71, '2022-11-07 21:06:36.333672', '3', 'Cubierta', 2, '[{"changed": {"fields": ["Activo"]}}]', 21, 1),
	(72, '2022-11-07 21:45:06.266748', '2', 'En proceso', 2, '[]', 21, 1),
	(73, '2022-11-16 16:50:46.143987', '11', 'Facturacion', 1, '[{"added": {}}]', 18, 1),
	(74, '2022-11-16 16:51:22.230263', '11', 'Facturación', 2, '[{"changed": {"fields": ["Title"]}}]', 18, 1),
	(75, '2022-11-17 14:22:02.956759', '16', 'Facturación', 1, '[{"added": {}}]', 21, 1),
	(76, '2022-11-17 14:23:17.774008', '16', 'Facturado', 2, '[{"changed": {"fields": ["Estatus", "Descripcion"]}}]', 21, 1),
	(77, '2022-11-17 14:25:07.528140', '15', 'Facturación', 2, '[{"changed": {"fields": ["Estatus", "Descripcion"]}}]', 21, 1),
	(78, '2022-11-22 22:03:07.931288', '1', 'Gerentes', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(79, '2022-11-22 22:04:12.899637', '1', 'Gerentes', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(80, '2022-11-22 22:16:10.982044', '3', 'gerente.ver', 2, '[{"changed": {"fields": ["Groups"]}}]', 16, 1),
	(81, '2022-11-22 22:17:34.813771', '3', 'gerente.ver', 2, '[{"changed": {"fields": ["password"]}}]', 16, 1),
	(82, '2022-11-22 22:37:51.658639', '9', 'Solicitudes', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Permissions granting access"]}}]', 18, 1),
	(83, '2022-11-22 22:38:28.019350', '10', 'Entrevistas', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Permissions granting access"]}}]', 18, 1),
	(84, '2022-11-22 22:39:09.845205', '11', 'Facturación', 2, '[{"changed": {"fields": ["Logged in only", "Permissions granting access"]}}]', 18, 1),
	(85, '2022-11-22 22:39:43.398935', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Logged in only", "Permissions granting access"]}}]', 18, 1),
	(86, '2022-11-22 22:40:08.637351', '4', 'Entidades', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Permissions granting access"]}}]', 18, 1),
	(87, '2022-11-22 22:41:42.872852', '3', 'Configuraciones', 2, '[{"changed": {"fields": ["Logged in only", "Permissions granting access"]}}]', 18, 1),
	(88, '2022-11-22 22:41:53.685215', '4', 'Entidades', 2, '[{"changed": {"fields": ["parent"]}}]', 18, 1),
	(89, '2022-11-22 22:42:14.449628', '5', 'Ciudades', 2, '[{"changed": {"fields": ["parent", "Permissions granting access"]}}]', 18, 1),
	(90, '2022-11-22 22:42:52.839952', '6', 'Locaciones', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Permissions granting access"]}}]', 18, 1),
	(91, '2022-11-22 22:43:19.694141', '7', 'Puestos', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Permissions granting access"]}}]', 18, 1),
	(92, '2022-11-22 22:44:46.387796', '8', 'Reclutamiento', 2, '[{"changed": {"fields": ["Logged in only", "Permissions granting access"]}}]', 18, 1),
	(93, '2022-11-22 22:45:26.228918', '8', 'Reclutamiento', 2, '[{"changed": {"fields": ["Permissions granting access"]}}]', 18, 1),
	(94, '2022-11-28 16:19:48.016963', '2', 'Proveedores', 1, '[{"added": {}}]', 3, 1),
	(95, '2022-11-28 16:25:14.526202', '3', 'RH Admin', 1, '[{"added": {}}]', 3, 1),
	(96, '2022-11-28 16:26:22.658556', '1', 'Gerentes', 2, '[]', 3, 1),
	(97, '2022-11-28 17:08:06.734462', '8', 'Reclutamiento', 2, '[{"changed": {"fields": ["Restrict access to permissions"]}}]', 18, 1),
	(98, '2022-11-28 17:08:28.735112', '8', 'Reclutamiento', 2, '[]', 18, 1),
	(99, '2022-11-28 17:09:01.573457', '9', 'Solicitudes', 2, '[{"changed": {"fields": ["parent", "Restrict access to permissions"]}}]', 18, 1),
	(100, '2022-11-28 17:09:17.701727', '10', 'Entrevistas', 2, '[{"changed": {"fields": ["parent", "Restrict access to permissions"]}}]', 18, 1),
	(101, '2022-11-28 17:09:32.715439', '10', 'Entrevistas', 2, '[{"changed": {"fields": ["parent"]}}]', 18, 1),
	(102, '2022-11-28 17:09:45.743297', '11', 'Facturación', 2, '[{"changed": {"fields": ["Restrict access to permissions"]}}]', 18, 1),
	(103, '2022-11-28 17:10:08.657526', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Restrict access to permissions"]}}]', 18, 1),
	(104, '2022-11-28 17:10:22.195620', '3', 'Configuraciones', 2, '[{"changed": {"fields": ["Restrict access to permissions"]}}]', 18, 1),
	(105, '2022-11-28 17:10:32.314489', '4', 'Entidades', 2, '[{"changed": {"fields": ["parent", "Restrict access to permissions"]}}]', 18, 1),
	(106, '2022-11-28 17:10:44.280782', '5', 'Ciudades', 2, '[{"changed": {"fields": ["parent", "Logged in only", "Restrict access to permissions"]}}]', 18, 1),
	(107, '2022-11-28 17:10:54.493863', '6', 'Locaciones', 2, '[{"changed": {"fields": ["parent", "Restrict access to permissions"]}}]', 18, 1),
	(108, '2022-11-28 17:11:03.485728', '7', 'Puestos', 2, '[{"changed": {"fields": ["parent", "Restrict access to permissions"]}}]', 18, 1),
	(109, '2022-11-28 17:11:41.853710', '1', 'Gerentes', 2, '[]', 3, 1),
	(110, '2022-11-28 17:12:42.179879', '1', 'Gerentes', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(111, '2022-11-28 17:13:36.226808', '1', 'Gerentes', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(112, '2022-11-28 17:13:58.525335', '1', 'Gerentes', 2, '[]', 3, 1),
	(113, '2022-11-28 17:14:15.717803', '6', 'Locaciones', 2, '[{"changed": {"fields": ["parent"]}}]', 18, 1),
	(114, '2022-11-28 17:14:33.755429', '3', 'Configuraciones', 2, '[]', 18, 1),
	(115, '2022-11-28 19:08:27.569617', '1', 'RH Gerentes', 2, '[{"changed": {"fields": ["Name"]}}]', 3, 1),
	(116, '2022-11-28 21:13:33.777407', '3', 'gerente.ver', 2, '[]', 16, 1),
	(117, '2022-11-28 21:13:56.374046', '1', 'RH Gerentes', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(118, '2022-11-28 22:03:40.595914', '4', 'corporativo.rh', 1, '[{"added": {}}]', 16, 1),
	(119, '2022-11-28 22:04:22.509365', '4', 'corporativo.rh', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Phone", "Groups"]}}]', 16, 1),
	(120, '2022-11-28 22:11:46.494644', '4', 'corporativo.rh', 2, '[{"changed": {"fields": ["Image"]}}]', 16, 1),
	(121, '2022-11-29 15:13:43.062066', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["First name", "Last name", "Groups"]}}]', 16, 1),
	(122, '2022-11-29 15:14:33.567039', '2', 'lsomohano20', 2, '[{"changed": {"fields": ["password"]}}]', 16, 1),
	(123, '2022-11-29 16:17:44.846510', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(124, '2022-11-29 16:22:59.914518', '2', 'Proveedores', 2, '[]', 3, 1),
	(125, '2022-11-29 16:45:37.440046', '2', 'lsomohano20', 2, '[]', 16, 1),
	(126, '2022-11-29 17:22:22.157701', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(127, '2022-11-29 17:29:36.813030', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(128, '2022-11-29 17:31:54.741543', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(129, '2022-11-29 17:40:41.266677', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1),
	(130, '2022-11-29 17:41:13.356622', '2', 'Proveedores', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.django_content_type: ~29 rows (aproximadamente)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(16, 'autenticacion', 'user'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(6, 'configuraciones', 'ciudades'),
	(12, 'configuraciones', 'contactos'),
	(7, 'configuraciones', 'entidades'),
	(8, 'configuraciones', 'locaciones'),
	(11, 'configuraciones', 'locacionespuestos'),
	(9, 'configuraciones', 'puestosnominas'),
	(10, 'configuraciones', 'puestosoperativos'),
	(4, 'contenttypes', 'contenttype'),
	(28, 'facturacion', 'facturas'),
	(29, 'facturacion', 'facturascandidatos'),
	(15, 'proveedores', 'contactosproveedores'),
	(14, 'proveedores', 'locacionesproveedores'),
	(13, 'proveedores', 'proveedores'),
	(5, 'sessions', 'session'),
	(17, 'sitetree', 'tree'),
	(18, 'sitetree', 'treeitem'),
	(23, 'solicitudes', 'candidatos'),
	(20, 'solicitudes', 'candidatosdocumentos'),
	(19, 'solicitudes', 'candidatosestatus'),
	(22, 'solicitudes', 'documentos'),
	(27, 'solicitudes', 'entrevistas'),
	(21, 'solicitudes', 'estatus'),
	(24, 'solicitudes', 'personas'),
	(25, 'solicitudes', 'solicitudesestatus'),
	(26, 'solicitudes', 'solicitudesvacantes');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.django_migrations: ~44 rows (aproximadamente)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2022-10-07 17:33:37.502011'),
	(2, 'contenttypes', '0002_remove_content_type_name', '2022-10-07 17:33:37.620830'),
	(3, 'auth', '0001_initial', '2022-10-07 17:33:38.050693'),
	(4, 'auth', '0002_alter_permission_name_max_length', '2022-10-07 17:33:38.096651'),
	(5, 'auth', '0003_alter_user_email_max_length', '2022-10-07 17:33:38.112817'),
	(6, 'auth', '0004_alter_user_username_opts', '2022-10-07 17:33:38.134202'),
	(7, 'auth', '0005_alter_user_last_login_null', '2022-10-07 17:33:38.154794'),
	(8, 'auth', '0006_require_contenttypes_0002', '2022-10-07 17:33:38.169619'),
	(9, 'auth', '0007_alter_validators_add_error_messages', '2022-10-07 17:33:38.187259'),
	(10, 'auth', '0008_alter_user_username_max_length', '2022-10-07 17:33:38.203132'),
	(11, 'auth', '0009_alter_user_last_name_max_length', '2022-10-07 17:33:38.218739'),
	(12, 'auth', '0010_alter_group_name_max_length', '2022-10-07 17:33:38.261989'),
	(13, 'auth', '0011_update_proxy_permissions', '2022-10-07 17:33:38.278113'),
	(14, 'auth', '0012_alter_user_first_name_max_length', '2022-10-07 17:33:38.293679'),
	(15, 'autenticacion', '0001_initial', '2022-10-07 17:33:38.908611'),
	(16, 'admin', '0001_initial', '2022-10-07 17:33:39.163877'),
	(17, 'admin', '0002_logentry_remove_auto_add', '2022-10-07 17:33:39.183962'),
	(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-07 17:33:39.206609'),
	(19, 'configuraciones', '0001_initial', '2022-10-07 17:33:40.640644'),
	(20, 'proveedores', '0001_initial', '2022-10-07 17:33:41.329782'),
	(21, 'sessions', '0001_initial', '2022-10-07 17:33:41.458099'),
	(22, 'sitetree', '0001_initial', '2022-10-07 17:33:42.573713'),
	(23, 'autenticacion', '0002_alter_user_image', '2022-10-11 16:25:36.387024'),
	(24, 'configuraciones', '0002_auto_20221011_1625', '2022-10-11 16:25:36.791545'),
	(25, 'proveedores', '0002_auto_20221011_1625', '2022-10-11 16:25:37.098062'),
	(26, 'solicitudes', '0001_initial', '2022-10-11 18:15:19.298963'),
	(27, 'solicitudes', '0002_auto_20221013_2202', '2022-10-13 22:02:29.540583'),
	(28, 'solicitudes', '0003_solicitudesvacantes_periodo_pago', '2022-10-13 22:12:39.974882'),
	(29, 'solicitudes', '0004_auto_20221018_1629', '2022-10-18 16:29:37.463247'),
	(30, 'solicitudes', '0005_rename_evalucion_psicometrica_candidatos_evaluacion_psicometrica', '2022-10-18 22:12:32.106385'),
	(31, 'solicitudes', '0006_auto_20221021_2220', '2022-10-21 22:20:39.194113'),
	(32, 'solicitudes', '0007_auto_20221031_1458', '2022-10-31 14:58:50.836342'),
	(33, 'configuraciones', '0003_locaciones_indicaciones_entrevista', '2022-11-02 22:23:51.726791'),
	(34, 'solicitudes', '0008_auto_20221102_2223', '2022-11-02 22:23:52.117669'),
	(35, 'solicitudes', '0009_auto_20221103_1657', '2022-11-03 16:57:26.273350'),
	(36, 'solicitudes', '0010_auto_20221104_1805', '2022-11-04 18:05:15.871191'),
	(37, 'solicitudes', '0011_auto_20221114_1701', '2022-11-14 17:02:24.731516'),
	(38, 'solicitudes', '0012_auto_20221115_1539', '2022-11-15 15:39:45.911543'),
	(39, 'configuraciones', '0004_auto_20221116_1629', '2022-11-16 16:29:38.877234'),
	(40, 'solicitudes', '0013_auto_20221116_1629', '2022-11-16 16:29:39.016970'),
	(41, 'proveedores', '0003_auto_20221116_1629', '2022-11-16 16:29:39.102693'),
	(42, 'facturacion', '0001_initial', '2022-11-16 16:29:39.754546'),
	(43, 'configuraciones', '0005_auto_20221124_1634', '2022-11-24 16:35:15.651609'),
	(44, 'facturacion', '0002_alter_facturas_pagado', '2022-11-24 16:35:15.708216');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.django_session: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('7cebbb32utsyjng2kzcudolas8to2b4w', '.eJxVjMsOwiAQRf-FtSFDh_Jw6d5vIAOMUjWQlHZl_HfbpAvd3nPOfYtA61LC2nkOUxZnocXpd4uUnlx3kB9U702mVpd5inJX5EG7vLbMr8vh_h0U6mWrgW7eGyYdMznvB1SjIvKODEVEGIFZAdvN0uiSyVYpFa1DBgQzYBKfL-T7N2U:1ozmKq:RgONb2BUjRA0ZbO_BV70tqKtcrFcssWpiVaEX5n9eHQ', '2022-12-12 22:10:44.566029'),
	('7hphlchb3vtn7tufvttyyf3q0vsjj5px', '.eJxVjEEOwiAQRe_C2hCYBpi6dO8ZyAwDUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izsur0uzGlR247kDu126zT3NZlYr0r-qBdX2fJz8vh_h1U6vVbE3gnPhBJBmGHwYC1ib3F0SMSEQOTCQ7NWFhyMQEKORgQvSQ3iHp_AO1eOCs:1p02Jd:4Yv9lpsJolUH9IcNqADpkmPdMZuIl4v6qazhspyIPgo', '2022-12-13 15:14:33.577919'),
	('f31oxn8v9j8mm5cvycu9vkuf1k00kq6p', '.eJxVjEEOwiAQRe_C2pBOCwO4dO8ZyDAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJY1ZnNajT75aIHzLtIN9pus2a52ldxqR3RR-06euc5Xk53L-DSq1-a8JUOA3QkREfLPRi0LDtnGTGTKb0GKRY78AVCIA-gQj7QGgHBGL1_gDxYjgP:1oxc1N:85BJWv9v07LCdBpKYB3DoUvGRPISoqUWqETxXv6_Ll0', '2022-12-06 22:45:41.985094'),
	('l28td9nhbr9lbryyy4hlogqnr4nim6fg', '.eJxVjEEOwiAQRe_C2hCYBpi6dO8ZyAwDUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izsur0uzGlR247kDu126zT3NZlYr0r-qBdX2fJz8vh_h1U6vVbE3gnPhBJBmGHwYC1ib3F0SMSEQOTCQ7NWFhyMQEKORgQvSQ3iHp_AO1eOCs:1or0vc:R3FzPExs0ZykkEJkE8jl4v3fC57etVf4j92_s6lGvwg', '2022-11-18 17:56:28.329250'),
	('q2el5h3kq38uigv7dsknhh63mjx7f0ov', '.eJxVjEEOwiAQRe_C2pBOCwO4dO8ZyDAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJY1ZnNajT75aIHzLtIN9pus2a52ldxqR3RR-06euc5Xk53L-DSq1-a8JUOA3QkREfLPRi0LDtnGTGTKb0GKRY78AVCIA-gQj7QGgHBGL1_gDxYjgP:1ozh7m:Hv5v4LBNLaAJHFuyPKi4qOpAbdHl4ivjxQsn8LyNDz0', '2022-12-12 16:36:54.118733'),
	('wy40p1m887jdob5wpnxq4kb27fz0n248', '.eJxVjEEOwiAQRe_C2hCYBpi6dO8ZyAwDUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izsur0uzGlR247kDu126zT3NZlYr0r-qBdX2fJz8vh_h1U6vVbE3gnPhBJBmGHwYC1ib3F0SMSEQOTCQ7NWFhyMQEKORgQvSQ3iHp_AO1eOCs:1oxbaA:NL830LNwW8kDB2WN1G-PWuomkcKNAcx6XTYodvoRh64', '2022-12-06 22:17:34.823102'),
	('x0n8rgnkf34fyqws7mwk1nvb2w21whsu', '.eJxVjDsOwjAQBe_iGll44xCbkj5nsN6ubRxAjpRPhbg7iZQC2pl5760C1qWEdU5TGKK6KlKnX8aQZ6q7iA_U-6hlrMs0sN4TfdhZ92NMr9vR_h0UzGVbS2eILtZEn01uOdvUJDpbRNOy9dwm14GdkJARNOTBcLB-gzDIEPX5AuwfONQ:1p02Jo:x0ocfqtm7b249ZxJPFpo5gJXT6V_qeMG-xViLO3r6pY', '2022-12-13 15:14:44.980886'),
	('xba4hjcs04vgceva028pd1unl96iuqic', '.eJxVjEEOwiAQRe_C2hCYBpi6dO8ZyAwDUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izsur0uzGlR247kDu126zT3NZlYr0r-qBdX2fJz8vh_h1U6vVbE3gnPhBJBmGHwYC1ib3F0SMSEQOTCQ7NWFhyMQEKORgQvSQ3iHp_AO1eOCs:1olvft:K1SxnHKWM6kJikoQUt1A6JOul-DZJtHP2yqHdgo3wcY', '2022-11-04 17:19:13.062763');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.documentos
CREATE TABLE IF NOT EXISTS `documentos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `documento` varchar(70) DEFAULT NULL,
  `descripcion` longtext,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `consideraciones` varchar(9) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.documentos: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` (`id`, `documento`, `descripcion`, `activo`, `created`, `updated`, `consideraciones`) VALUES
	(1, 'Acta de nacimiento', '*', 'Y', '2022-10-28 21:48:12.641578', '2022-10-28 21:48:12.641611', 'requerido'),
	(2, 'Credencial de elector', '*', 'Y', '2022-10-28 21:48:33.481194', '2022-10-28 21:48:33.481225', 'requerido'),
	(3, 'CURP', '*', 'Y', '2022-10-28 21:48:45.178714', '2022-10-28 21:48:45.178745', 'requerido'),
	(4, 'Numero de seguro social', 'De la pagina oficial del IMSS', 'Y', '2022-10-28 21:49:13.997197', '2022-10-28 21:49:13.997231', 'requerido'),
	(5, 'Comprobante de Domicilio', '(Preferente recibo de CFE), no mayor a tres meses', 'Y', '2022-10-28 21:50:17.169486', '2022-10-28 21:50:17.169521', 'requerido'),
	(6, 'Aviso de retenciones Infonavit', '*', 'Y', '2022-10-28 21:51:21.587773', '2022-10-28 21:51:21.587816', 'opcional'),
	(7, 'Estado de cuenta FONACOT', 'En caso de tener crédito vigente', 'Y', '2022-10-28 21:52:07.021169', '2022-10-28 21:52:07.021201', 'opcional'),
	(8, 'RFC', 'Situación fiscal sueldos y salarios e ingresos asimilados a salarios (2 hojas SAT)', 'Y', '2022-10-28 21:53:30.651606', '2022-10-28 21:53:30.651667', 'requerido'),
	(9, 'Curriculum Vitae', '*', 'Y', '2022-10-28 21:54:12.645440', '2022-10-28 21:54:12.645472', 'requerido'),
	(10, 'Solicitud de empleo', '*', 'Y', '2022-10-28 21:54:35.345591', '2022-10-28 21:54:35.345622', 'requerido'),
	(11, 'Licencia de conducir', 'Vigente', 'Y', '2022-10-28 21:54:53.958624', '2022-10-28 21:54:53.958655', 'requerido'),
	(12, 'Cartilla militar', '*', 'Y', '2022-10-28 21:55:12.293463', '2022-10-28 21:55:12.293498', 'requerido'),
	(13, 'Comprobante de estudios', '*', 'Y', '2022-10-28 21:55:48.333348', '2022-10-28 21:55:48.333379', 'requerido'),
	(14, 'Constancias laborales', 'Constancias de los últimos tres empleos', 'Y', '2022-10-28 21:56:25.665256', '2022-10-28 21:56:25.665288', 'requerido'),
	(15, 'Afore', '*', 'Y', '2022-10-28 21:56:43.116049', '2022-10-28 21:56:43.116078', 'requerido'),
	(16, 'Antecedentes no penales', 'Documento original', 'Y', '2022-10-28 21:57:09.683884', '2022-10-28 21:57:09.683919', 'requerido'),
	(17, 'Fotos tamaño infantil', '*', 'Y', '2022-10-28 21:57:43.171755', '2022-10-28 21:57:43.171788', 'opcional');
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.entidades
CREATE TABLE IF NOT EXISTS `entidades` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `entidad` varchar(70) NOT NULL,
  `pais` varchar(2) NOT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.entidades: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `entidades` DISABLE KEYS */;
INSERT INTO `entidades` (`id`, `entidad`, `pais`, `activo`, `created`, `updated`) VALUES
	(1, 'Quintana Roo', 'mx', 'Y', '2022-10-07 23:18:34.401150', '2022-10-07 23:18:34.401205'),
	(2, 'Veracruz', 'mx', 'Y', '2022-10-07 23:18:43.750764', '2022-10-07 23:18:43.750801');
/*!40000 ALTER TABLE `entidades` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.entrevistas
CREATE TABLE IF NOT EXISTS `entrevistas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `indicaciones` longtext,
  `created` datetime(6) NOT NULL,
  `fecha_programada` date NOT NULL,
  `hora_programada` time(6) NOT NULL,
  `fecha_entrevista` datetime(6) DEFAULT NULL,
  `asistio` varchar(1) DEFAULT NULL,
  `candidatos_id` bigint(20) NOT NULL,
  `tipo_evento` varchar(12) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `entrevistas_candidatos_id_54ee1c16_fk_candidatos_id` (`candidatos_id`),
  CONSTRAINT `entrevistas_candidatos_id_54ee1c16_fk_candidatos_id` FOREIGN KEY (`candidatos_id`) REFERENCES `candidatos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.entrevistas: ~12 rows (aproximadamente)
/*!40000 ALTER TABLE `entrevistas` DISABLE KEYS */;
INSERT INTO `entrevistas` (`id`, `indicaciones`, `created`, `fecha_programada`, `hora_programada`, `fecha_entrevista`, `asistio`, `candidatos_id`, `tipo_evento`) VALUES
	(2, 'T', '2022-11-03 15:21:52.000000', '2022-11-04', '15:22:01.000000', NULL, 'N', 1, 'entrevista'),
	(3, 'Esta es la segunda vez que se agenda a entrevista', '2022-11-08 21:25:11.468773', '2022-11-09', '16:24:00.000000', '2022-11-09 00:00:00.000000', 'Y', 1, 'entrevista'),
	(4, 'comentarios', '2022-11-14 16:51:26.409300', '2022-11-18', '11:51:00.000000', '2022-11-14 00:00:00.000000', 'Y', 3, 'entrevista'),
	(6, 'comentarios.', '2022-11-14 17:34:12.188702', '2022-11-18', '11:51:00.000000', '2022-11-18 21:10:03.079417', 'N', 4, 'entrevista'),
	(7, 'n', '2022-11-15 15:48:41.340752', '2022-11-17', '10:48:00.000000', '2022-11-23 22:29:51.355532', 'Y', 5, 'entrevista'),
	(8, 'r', '2022-11-15 16:06:08.250222', '2022-11-19', '11:06:00.000000', '2022-11-15 17:40:12.722325', 'Y', 1, 'contratacion'),
	(9, 'ok', '2022-11-18 19:17:34.349326', '2022-11-19', '11:21:00.000000', '2022-11-18 19:17:55.515065', 'Y', 3, 'contratacion'),
	(10, 'f', '2022-11-20 00:34:14.708881', '2022-11-19', '11:42:00.000000', '2022-11-20 00:34:27.473177', 'Y', 4, 'entrevista'),
	(11, 'f', '2022-11-20 00:34:47.692813', '2022-11-19', '11:21:00.000000', '2022-11-20 00:35:08.055629', 'Y', 4, 'contratacion'),
	(12, 'se va en transporte de la empresa', '2022-11-23 22:13:54.048705', '2022-11-24', '11:51:00.000000', '2022-11-23 22:18:07.047153', 'Y', 6, 'entrevista'),
	(13, 'rewiriryr', '2022-11-23 22:20:03.727240', '2022-11-25', '09:19:00.000000', '2022-11-23 22:20:53.913605', 'Y', 6, 'contratacion'),
	(14, 'ccc', '2022-11-23 22:30:29.759967', '2022-11-25', '17:30:00.000000', '2022-11-23 22:33:56.955550', 'Y', 5, 'contratacion'),
	(15, 'ok', '2022-11-29 18:14:58.912753', '2022-11-30', '13:14:00.000000', '2022-11-29 18:31:52.628247', 'Y', 7, 'entrevista'),
	(16, 'ok', '2022-11-29 20:37:19.978404', '2022-12-03', '14:04:00.000000', '2022-11-29 22:00:58.929843', 'Y', 7, 'contratacion'),
	(17, 'd', '2022-11-29 22:18:55.462652', '2022-11-23', '17:18:00.000000', NULL, NULL, 7, 'ingreso');
/*!40000 ALTER TABLE `entrevistas` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.facturas
CREATE TABLE IF NOT EXISTS `facturas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_ini` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `pre_factura_pdf` varchar(100) DEFAULT NULL,
  `pre_factura_xml` varchar(100) DEFAULT NULL,
  `factura_pdf` varchar(100) DEFAULT NULL,
  `factura_xml` varchar(100) DEFAULT NULL,
  `total_facturado` decimal(20,2) DEFAULT NULL,
  `activo` varchar(1) NOT NULL,
  `pagado` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `proveedores_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas_proveedores_id_b77b84de_fk_proveedores_id` (`proveedores_id`),
  CONSTRAINT `facturas_proveedores_id_b77b84de_fk_proveedores_id` FOREIGN KEY (`proveedores_id`) REFERENCES `proveedores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.facturas: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` (`id`, `fecha_ini`, `fecha_fin`, `pre_factura_pdf`, `pre_factura_xml`, `factura_pdf`, `factura_xml`, `total_facturado`, `activo`, `pagado`, `created`, `updated`, `proveedores_id`) VALUES
	(1, '2020-11-20', '2020-11-20', 'prefacturas/pdf/3_.pdf', 'prefacturas/xml/2_.pdf', 'facturas/pdf/2_.pdf', 'facturas/xml/2__dmtHDNe.pdf', 10000000.00, 'Y', 'Y', '2022-11-16 21:32:08.633531', '2022-11-22 19:15:52.906938', 1),
	(2, '2020-11-20', '2020-11-20', 'prefacturas/pdf/3__H0nZ6Ri.pdf', 'prefacturas/xml/1__zMssBEg.pdf', 'facturas/pdf/1_.pdf', 'facturas/xml/carta.pdf', 20000.00, 'Y', 'N', '2022-11-19 22:42:53.957776', '2022-11-20 00:42:31.337185', 1),
	(3, '2020-11-20', '2020-11-20', 'prefacturas/pdf/1_.pdf', 'prefacturas/xml/3_.pdf', 'facturas/pdf/3__M23Lecy.pdf', 'facturas/xml/2__1diOgmv.pdf', 70000.00, 'Y', 'Y', '2022-11-23 22:52:46.141310', '2022-11-23 22:55:54.731717', 1);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.facturas_candidatos
CREATE TABLE IF NOT EXISTS `facturas_candidatos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `candidatos_id` bigint(20) NOT NULL,
  `facturas_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas_candidatos_candidatos_id_4fb6bbc4_fk_candidatos_id` (`candidatos_id`),
  KEY `facturas_candidatos_facturas_id_62fd8eb3_fk_facturas_id` (`facturas_id`),
  CONSTRAINT `facturas_candidatos_candidatos_id_4fb6bbc4_fk_candidatos_id` FOREIGN KEY (`candidatos_id`) REFERENCES `candidatos` (`id`),
  CONSTRAINT `facturas_candidatos_facturas_id_62fd8eb3_fk_facturas_id` FOREIGN KEY (`facturas_id`) REFERENCES `facturas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.facturas_candidatos: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `facturas_candidatos` DISABLE KEYS */;
INSERT INTO `facturas_candidatos` (`id`, `activo`, `created`, `updated`, `candidatos_id`, `facturas_id`) VALUES
	(1, 'Y', '2022-11-18 22:06:56.004054', '2022-11-18 22:06:56.007391', 1, 1),
	(2, 'Y', '2022-11-18 22:06:56.011675', '2022-11-18 22:06:56.013719', 3, 1),
	(3, 'Y', '2022-11-20 00:35:22.288459', '2022-11-20 00:35:22.293295', 4, 2),
	(4, 'Y', '2022-11-23 22:53:43.112744', '2022-11-23 22:53:43.115892', 5, 3),
	(5, 'Y', '2022-11-23 22:53:43.127223', '2022-11-23 22:53:43.129875', 6, 3);
/*!40000 ALTER TABLE `facturas_candidatos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.locaciones
CREATE TABLE IF NOT EXISTS `locaciones` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `locacion` varchar(6) NOT NULL,
  `locacion_name` varchar(100) NOT NULL,
  `direccion` longtext NOT NULL,
  `codigo_postal` varchar(5) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `latitud` varchar(15) NOT NULL,
  `longitud` varchar(15) NOT NULL,
  `horario_apertura` time(6) NOT NULL,
  `horario_cierre` time(6) NOT NULL,
  `dias_operativos` varchar(50) NOT NULL,
  `zona_ciudad` varchar(10) NOT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `ciudades_id` bigint(20) NOT NULL,
  `indicaciones_entrevista` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `locaciones_ciudades_id_c43c2383_fk_ciudades_id` (`ciudades_id`),
  CONSTRAINT `locaciones_ciudades_id_c43c2383_fk_ciudades_id` FOREIGN KEY (`ciudades_id`) REFERENCES `ciudades` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.locaciones: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `locaciones` DISABLE KEYS */;
INSERT INTO `locaciones` (`id`, `locacion`, `locacion_name`, `direccion`, `codigo_postal`, `telefono`, `email`, `latitud`, `longitud`, `horario_apertura`, `horario_cierre`, `dias_operativos`, `zona_ciudad`, `activo`, `created`, `updated`, `ciudades_id`, `indicaciones_entrevista`) VALUES
	(1, 'CAN50', 'HERTZ CANCUN AEOROPUERTO', 'x', '74589', '7412536895', 'prueba@email.com', '21.040796', '-99.2050712', '06:00:00.000000', '18:00:00.000000', 'lun,Mar,Mie,Jue,Vie', 'aeropuerto', 'Y', '2022-10-07 23:20:30.190991', '2022-10-07 23:20:30.191019', 1, 'locaciones/indicaciones/3_.pdf'),
	(2, 'VER50', 'Hertz Veracruz Aeropuerto', 'x', '74859', '478512369', 'email@email.com', '19.4388173', '-99.2050712', '06:00:00.000000', '18:00:00.000000', 'lun,Mar,Mie,Jue,Vie', 'aeropuerto', 'Y', '2022-10-13 15:01:53.983834', '2022-10-13 15:01:53.983860', 3, 'locaciones/indicaciones/2_.pdf'),
	(3, 'PDC50', 'HERTZ PLAYA DEL CARMEN', 'stree 80 m 26 l2', '77528', '9982140871', 'lsomohano20@gmail.com', '21.040796', '-99.2050712', '06:00:00.000000', '17:00:00.000000', 'lun,Mar,Mie,Jue,Vie', 'ciudad', 'Y', '2022-11-04 17:40:22.077136', '2022-11-04 17:40:22.077166', 2, 'locaciones/indicaciones/1_.pdf');
/*!40000 ALTER TABLE `locaciones` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.locaciones_proveedores
CREATE TABLE IF NOT EXISTS `locaciones_proveedores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `locaciones_id` bigint(20) NOT NULL,
  `proveedores_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `locaciones_proveedores_locaciones_id_bb6efec6_fk_locaciones_id` (`locaciones_id`),
  KEY `locaciones_proveedores_proveedores_id_cbc69730_fk_proveedores_id` (`proveedores_id`),
  CONSTRAINT `locaciones_proveedores_locaciones_id_bb6efec6_fk_locaciones_id` FOREIGN KEY (`locaciones_id`) REFERENCES `locaciones` (`id`),
  CONSTRAINT `locaciones_proveedores_proveedores_id_cbc69730_fk_proveedores_id` FOREIGN KEY (`proveedores_id`) REFERENCES `proveedores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.locaciones_proveedores: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `locaciones_proveedores` DISABLE KEYS */;
INSERT INTO `locaciones_proveedores` (`id`, `activo`, `created`, `updated`, `locaciones_id`, `proveedores_id`) VALUES
	(1, 'Y', '2022-11-09 15:45:53.162346', '2022-11-09 15:45:53.162381', 2, 1);
/*!40000 ALTER TABLE `locaciones_proveedores` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.locaciones_puestos
CREATE TABLE IF NOT EXISTS `locaciones_puestos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `staf_requerido` int(11) DEFAULT NULL,
  `staf_contratado` int(11) DEFAULT NULL,
  `activo` varchar(5) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `locaciones_id` bigint(20) NOT NULL,
  `puestos_operativos_id` bigint(20) NOT NULL,
  `staf_autorizado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `locaciones_puestos_locaciones_id_8790d0fc_fk_locaciones_id` (`locaciones_id`),
  KEY `locaciones_puestos_puestos_operativos_i_241ad7ea_fk_puestos_o` (`puestos_operativos_id`),
  CONSTRAINT `locaciones_puestos_locaciones_id_8790d0fc_fk_locaciones_id` FOREIGN KEY (`locaciones_id`) REFERENCES `locaciones` (`id`),
  CONSTRAINT `locaciones_puestos_puestos_operativos_i_241ad7ea_fk_puestos_o` FOREIGN KEY (`puestos_operativos_id`) REFERENCES `puestos_operativos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.locaciones_puestos: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `locaciones_puestos` DISABLE KEYS */;
INSERT INTO `locaciones_puestos` (`id`, `staf_requerido`, `staf_contratado`, `activo`, `created`, `updated`, `locaciones_id`, `puestos_operativos_id`, `staf_autorizado`) VALUES
	(1, 2, 0, 'Y', '2022-10-11 16:47:04.277302', '2022-11-24 17:42:00.169728', 1, 3, 2),
	(2, 5, 3, 'Y', '2022-10-12 22:06:56.781999', '2022-11-24 17:41:36.646835', 1, 2, 1),
	(3, 3, 2, 'Y', '2022-10-13 15:03:37.910474', '2022-10-13 15:03:37.910506', 2, 3, 0),
	(4, 2, 1, 'Y', '2022-11-09 15:44:10.102461', '2022-11-24 17:41:48.960671', 1, 1, 1);
/*!40000 ALTER TABLE `locaciones_puestos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.personas
CREATE TABLE IF NOT EXISTS `personas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido_paterno` varchar(100) DEFAULT NULL,
  `apellido_materno` varchar(100) DEFAULT NULL,
  `rfc` varchar(20) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `telefono` varchar(15) NOT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `genero` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rfc` (`rfc`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.personas: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` (`id`, `nombre`, `apellido_paterno`, `apellido_materno`, `rfc`, `fecha_nacimiento`, `email`, `telefono`, `activo`, `created`, `updated`, `genero`) VALUES
	(1, 'Leonel', 'Somohano', 'Carmona', 'SOCL850309JD8', '2022-10-05', 'lsomohano20@gmail.com', '9982140871', 'Y', '2022-11-01 16:02:12.202437', '2022-11-01 16:02:12.202466', 'M'),
	(2, 'Marco', 'Garcia', 'Bueno', 'XEXX010101000', '2009-06-05', 'marco@email.com', '784571236', 'Y', '2022-11-09 23:26:22.402311', '2022-11-09 23:26:22.402364', 'M'),
	(3, 'Marco', 'Garcia', 'Bueno', 'XEXX010101002', '2005-06-20', 'marco@email.com', '784571236', 'Y', '2022-11-09 23:27:57.363111', '2022-11-09 23:27:57.363141', 'M'),
	(4, 'Ruben', 'Sanchez', 'Sambrano', 'XEXX010101014', '2020-11-20', 'lsomohano20@gmail.com', '+529982140871', 'Y', '2022-11-14 17:11:21.080302', '2022-11-20 00:34:27.470555', 'M'),
	(5, 'Leonel', 'Somohano', 'Carmona', 'XEXX010101005', '2017-02-19', 'lsomohano20@gmail.com', '+529982140871', 'Y', '2022-11-15 15:47:54.870857', '2022-11-23 22:29:51.353915', 'M'),
	(6, 'Marcos', 'Sambrano', 'Ochoa', 'XEXX010101058', '2005-05-19', 'email@email.com', '74581236', 'Y', '2022-11-23 22:05:53.469374', '2022-11-23 22:18:07.045344', 'M'),
	(7, 'Leonel', 'Somohano', 'Carmona', 'XEXX010101016', '2022-11-15', 'lsomohano20@gmail.com', '+529982140871', 'Y', '2022-11-28 15:49:27.396129', '2022-11-29 18:31:52.624975', 'M');
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `proveedor` varchar(70) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `razon_social` varchar(200) DEFAULT NULL,
  `direccion` longtext,
  `codigo_postal` varchar(5) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.proveedores: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` (`id`, `proveedor`, `rfc`, `razon_social`, `direccion`, `codigo_postal`, `telefono`, `email`, `activo`, `created`, `updated`) VALUES
	(1, 'Proveedor Veracruz', 'SOCL850309JD8', 'Proveedor de prueba SA de CVk', 'stree 80 m 26 l2', '77528', '9982140871', 'lsomohano20@gmail.com', 'Y', '2022-11-09 15:45:09.093690', '2022-11-16 18:40:32.226214');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.puestos_nominas
CREATE TABLE IF NOT EXISTS `puestos_nominas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `puesto_nomina` varchar(60) NOT NULL,
  `activo` varchar(5) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.puestos_nominas: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `puestos_nominas` DISABLE KEYS */;
INSERT INTO `puestos_nominas` (`id`, `puesto_nomina`, `activo`, `created`, `updated`) VALUES
	(1, 'Auxiliar de Servicios', 'Y', '2022-10-07 23:21:10.700172', '2022-10-07 23:21:10.700206'),
	(2, 'Auxiliar Administrativo', 'N', '2022-10-07 23:22:59.135218', '2022-11-22 22:18:37.149955'),
	(3, 'Auxiliar Administrativo', 'N', '2022-10-07 23:23:55.141232', '2022-10-07 23:23:55.141270');
/*!40000 ALTER TABLE `puestos_nominas` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.puestos_operativos
CREATE TABLE IF NOT EXISTS `puestos_operativos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `puesto_operativo` varchar(60) NOT NULL,
  `canal_reclutamiento` varchar(7) NOT NULL,
  `activo` varchar(5) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `puestos_nominas_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `puestos_operativos_puestos_nominas_id_317591f8_fk_puestos_n` (`puestos_nominas_id`),
  CONSTRAINT `puestos_operativos_puestos_nominas_id_317591f8_fk_puestos_n` FOREIGN KEY (`puestos_nominas_id`) REFERENCES `puestos_nominas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.puestos_operativos: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `puestos_operativos` DISABLE KEYS */;
INSERT INTO `puestos_operativos` (`id`, `puesto_operativo`, `canal_reclutamiento`, `activo`, `created`, `updated`, `puestos_nominas_id`) VALUES
	(1, 'Soporte técnico TI', 'externo', 'N', '2022-10-07 23:24:19.449335', '2022-11-22 22:18:24.600274', 2),
	(2, 'Salas', 'externo', 'Y', '2022-10-07 23:24:43.843632', '2022-10-07 23:24:43.843664', 1),
	(3, 'Trasladista', 'externo', 'Y', '2022-10-07 23:24:59.306969', '2022-10-07 23:24:59.307005', 1);
/*!40000 ALTER TABLE `puestos_operativos` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.sitetree_tree
CREATE TABLE IF NOT EXISTS `sitetree_tree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `alias` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias` (`alias`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.sitetree_tree: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `sitetree_tree` DISABLE KEYS */;
INSERT INTO `sitetree_tree` (`id`, `title`, `alias`) VALUES
	(1, 'Avasa RH', 'AvasaRH');
/*!40000 ALTER TABLE `sitetree_tree` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.sitetree_treeitem
CREATE TABLE IF NOT EXISTS `sitetree_treeitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `hint` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  `urlaspattern` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `alias` varchar(80) DEFAULT NULL,
  `description` longtext NOT NULL,
  `inmenu` tinyint(1) NOT NULL,
  `inbreadcrumbs` tinyint(1) NOT NULL,
  `insitetree` tinyint(1) NOT NULL,
  `access_loggedin` tinyint(1) NOT NULL,
  `access_guest` tinyint(1) NOT NULL,
  `access_restricted` tinyint(1) NOT NULL,
  `access_perm_type` int(11) NOT NULL,
  `sort_order` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `tree_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sitetree_treeitem_tree_id_alias_f597fbd9_uniq` (`tree_id`,`alias`),
  KEY `sitetree_treeitem_parent_id_88f6f9a4_fk_sitetree_treeitem_id` (`parent_id`),
  KEY `sitetree_treeitem_url_b91ef35a` (`url`),
  KEY `sitetree_treeitem_urlaspattern_ff432a51` (`urlaspattern`),
  KEY `sitetree_treeitem_hidden_5de28c6e` (`hidden`),
  KEY `sitetree_treeitem_alias_33dc5690` (`alias`),
  KEY `sitetree_treeitem_inmenu_ccabc0b0` (`inmenu`),
  KEY `sitetree_treeitem_inbreadcrumbs_ebb24448` (`inbreadcrumbs`),
  KEY `sitetree_treeitem_insitetree_60c593a5` (`insitetree`),
  KEY `sitetree_treeitem_access_loggedin_8a523197` (`access_loggedin`),
  KEY `sitetree_treeitem_access_guest_09916132` (`access_guest`),
  KEY `sitetree_treeitem_access_restricted_e9c87676` (`access_restricted`),
  KEY `sitetree_treeitem_sort_order_93fd716c` (`sort_order`),
  CONSTRAINT `sitetree_treeitem_parent_id_88f6f9a4_fk_sitetree_treeitem_id` FOREIGN KEY (`parent_id`) REFERENCES `sitetree_treeitem` (`id`),
  CONSTRAINT `sitetree_treeitem_tree_id_038a4bc7_fk_sitetree_tree_id` FOREIGN KEY (`tree_id`) REFERENCES `sitetree_tree` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.sitetree_treeitem: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `sitetree_treeitem` DISABLE KEYS */;
INSERT INTO `sitetree_treeitem` (`id`, `title`, `hint`, `url`, `urlaspattern`, `hidden`, `alias`, `description`, `inmenu`, `inbreadcrumbs`, `insitetree`, `access_loggedin`, `access_guest`, `access_restricted`, `access_perm_type`, `sort_order`, `parent_id`, `tree_id`) VALUES
	(1, 'Dashboard', '', 'Home', 1, 0, NULL, '', 1, 1, 1, 0, 0, 0, 1, 1, NULL, 1),
	(2, 'Proveedores', '', 'Proveedores', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 8, NULL, 1),
	(3, 'Configuraciones', '', '#', 0, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 11, NULL, 1),
	(4, 'Entidades', '', 'Entidades', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 4, 3, 1),
	(5, 'Ciudades', '', 'Ciudades', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 5, 3, 1),
	(6, 'Locaciones', '', 'Locaciones', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 6, 3, 1),
	(7, 'Puestos', '', 'Puestos', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 7, 3, 1),
	(8, 'Reclutamiento', '', '#', 0, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 2, NULL, 1),
	(9, 'Solicitudes', '', 'Solicitudes', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 9, 8, 1),
	(10, 'Entrevistas', '', 'Entrevistas', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 10, 8, 1),
	(11, 'Facturación', '', 'Facturacion', 1, 0, NULL, '', 1, 1, 1, 1, 0, 1, 1, 3, NULL, 1);
/*!40000 ALTER TABLE `sitetree_treeitem` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.sitetree_treeitem_access_permissions
CREATE TABLE IF NOT EXISTS `sitetree_treeitem_access_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `treeitem_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sitetree_treeitem_access_treeitem_id_permission_i_a3224a96_uniq` (`treeitem_id`,`permission_id`),
  KEY `sitetree_treeitem_ac_permission_id_c6d1d87a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `sitetree_treeitem_ac_permission_id_c6d1d87a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `sitetree_treeitem_ac_treeitem_id_aedb7367_fk_sitetree_` FOREIGN KEY (`treeitem_id`) REFERENCES `sitetree_treeitem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.sitetree_treeitem_access_permissions: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `sitetree_treeitem_access_permissions` DISABLE KEYS */;
INSERT INTO `sitetree_treeitem_access_permissions` (`id`, `treeitem_id`, `permission_id`) VALUES
	(4, 2, 56),
	(11, 3, 24),
	(12, 3, 28),
	(6, 3, 32),
	(7, 3, 36),
	(8, 3, 40),
	(9, 3, 44),
	(10, 3, 48),
	(5, 4, 28),
	(13, 5, 24),
	(14, 6, 32),
	(15, 7, 36),
	(16, 8, 104),
	(17, 8, 108),
	(1, 9, 104),
	(2, 10, 108),
	(3, 11, 112);
/*!40000 ALTER TABLE `sitetree_treeitem_access_permissions` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.solicitudes_estatus
CREATE TABLE IF NOT EXISTS `solicitudes_estatus` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `estatus_id` bigint(20) NOT NULL,
  `solicitudes_vacantes_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `solicitudes_estatus_estatus_id_37e03d68_fk_calogos_estatus_id` (`estatus_id`),
  KEY `solicitudes_estatus_solicitudes_vacantes_f4bdb182_fk_solicitud` (`solicitudes_vacantes_id`),
  CONSTRAINT `solicitudes_estatus_estatus_id_37e03d68_fk_calogos_estatus_id` FOREIGN KEY (`estatus_id`) REFERENCES `calogos_estatus` (`id`),
  CONSTRAINT `solicitudes_estatus_solicitudes_vacantes_f4bdb182_fk_solicitud` FOREIGN KEY (`solicitudes_vacantes_id`) REFERENCES `solicitudes_vacantes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.solicitudes_estatus: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `solicitudes_estatus` DISABLE KEYS */;
INSERT INTO `solicitudes_estatus` (`id`, `activo`, `created`, `updated`, `estatus_id`, `solicitudes_vacantes_id`) VALUES
	(1, 'N', '2022-10-14 21:33:16.116937', '2022-10-14 21:33:16.116973', 1, 1),
	(2, 'N', '2022-10-18 18:15:33.751059', '2022-10-18 18:15:33.751090', 1, 2),
	(3, 'Y', '2022-10-21 22:44:52.813549', '2022-10-21 22:44:52.813579', 1, 3),
	(4, 'Y', '2022-11-01 16:02:12.314339', '2022-11-01 16:02:12.314372', 2, 1),
	(5, 'N', '2022-11-09 15:47:07.482161', '2022-11-09 15:47:07.482228', 1, 4),
	(6, 'Y', '2022-11-15 15:47:55.027747', '2022-11-15 15:47:55.027778', 2, 2),
	(7, 'Y', '2022-11-23 22:05:53.601552', '2022-11-23 22:05:53.602930', 2, 4);
/*!40000 ALTER TABLE `solicitudes_estatus` ENABLE KEYS */;

-- Volcando estructura para tabla rhdb_dev.solicitudes_vacantes
CREATE TABLE IF NOT EXISTS `solicitudes_vacantes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sueldos` decimal(20,2) NOT NULL,
  `comiciones` varchar(1) NOT NULL,
  `bono` varchar(1) NOT NULL,
  `garantia` varchar(1) NOT NULL,
  `activo` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `locaciones_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `periodo_pago` varchar(10) NOT NULL,
  `puestos_operativos_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `solicitudes_vacantes_locaciones_id_7ccc0fb6_fk_locaciones_id` (`locaciones_id`),
  KEY `solicitudes_vacantes_user_id_03648159_fk_autenticacion_user_id` (`user_id`),
  KEY `solicitudes_vacantes_puestos_operativos_i_a98f0900_fk_puestos_o` (`puestos_operativos_id`),
  CONSTRAINT `solicitudes_vacantes_locaciones_id_7ccc0fb6_fk_locaciones_id` FOREIGN KEY (`locaciones_id`) REFERENCES `locaciones` (`id`),
  CONSTRAINT `solicitudes_vacantes_puestos_operativos_i_a98f0900_fk_puestos_o` FOREIGN KEY (`puestos_operativos_id`) REFERENCES `puestos_operativos` (`id`),
  CONSTRAINT `solicitudes_vacantes_user_id_03648159_fk_autenticacion_user_id` FOREIGN KEY (`user_id`) REFERENCES `autenticacion_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla rhdb_dev.solicitudes_vacantes: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `solicitudes_vacantes` DISABLE KEYS */;
INSERT INTO `solicitudes_vacantes` (`id`, `sueldos`, `comiciones`, `bono`, `garantia`, `activo`, `created`, `updated`, `locaciones_id`, `user_id`, `cantidad`, `periodo_pago`, `puestos_operativos_id`) VALUES
	(1, 1200.00, 'N', 'Y', 'Y', 'Y', '2022-10-14 21:33:16.107760', '2022-10-14 21:33:16.107796', 2, 3, 3, 'quincenal', 2),
	(2, 333333.00, 'Y', 'Y', 'Y', 'Y', '2022-10-18 18:15:33.738351', '2022-10-18 18:15:33.738383', 1, 1, 1, 'quincenal', 3),
	(3, 12000.00, 'Y', 'Y', 'Y', 'Y', '2022-10-21 22:44:52.805657', '2022-10-21 22:44:52.805688', 1, 1, 2, 'quincenal', 1),
	(4, 12220.00, 'Y', 'Y', 'Y', 'Y', '2022-11-09 15:47:07.472449', '2022-11-09 15:47:07.472482', 3, 1, 1, 'quincenal', 3);
/*!40000 ALTER TABLE `solicitudes_vacantes` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
