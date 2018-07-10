ALTER TABLE `example` ADD `location` VARCHAR(200) NOT NULL AFTER `description`;


INSERT INTO `test-catma`.`Router` (`ID`, `SysDescription`, `Hostname`, `TotalInterface`, `MemoryUse`, `MemoryFree`, `NVRAMSize`, `NVRAMUsed`, `PowerSupplyDesc`, `VoltageValue`, `Location`) VALUES (NULL, 'Example description for router.', 'Example host-name for router.', '8', '9999', '99999', '88888', '8888', '353535', '101010', 'Example Location for router.')



"INSERT INTO "+table_name+" VALUES (NULL, '"+SysDesc+"', '"+hostname+"', '"+totalInt+"', '"+MemoryUse+"', '"+MemoryFree+"', '"+NvramSize+"', '"+NvramUsed+"', '"+power+"', '"+vol+"', '"+location+"')"