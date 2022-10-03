CREATE DEFINER=`root`@`localhost` PROCEDURE `vwap`(userinput datetime)
BEGIN
set @userinput1 = userinput;
                
select sum(`<vol>`*`<close>`)/sum(`<vol>`),@userinput1 , addtime(`<date>`, "5:0:0") as "End time"  FROM sd2
where `<date>` between @userinput1 AND addtime(`<date>`, "5:0:0");
                
END