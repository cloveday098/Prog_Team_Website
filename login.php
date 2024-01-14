<?php
  $host = 'localhost';
  $user = 'root';
  $pass = 'root';
  $data = 'progteam';
  $chrs = 'utf8mb4';
  $attr = "mysql:host=$host;dbname=$data;charset=$chrs";
  $db_port = 8889;
  $opts = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE  => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES  => false
  ];

  
?>	
