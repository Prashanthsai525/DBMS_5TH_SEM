DELIMITER $$
CREATE PROCEDURE view_people_involved()
begin
-- select c.criminal_name,cr.crime_type,f.fir_statement,f.fir_writer from crime as cr inner join criminal as c on cr.crime_id=c.crime_id inner join fir as f on c.crime_id=cr.crime_id;
select c.criminal_name,cr.crime_type,f.fir_statement,f.fir_writer from crime as cr NATURAL JOIN (criminal as c NATURAL JOIN fir as f);
end $$
DELIMITER ;