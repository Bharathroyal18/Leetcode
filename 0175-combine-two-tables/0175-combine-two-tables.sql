select P.firstName,P.lastName,A.city,A.state From Person P
left join Address A
on p.personid=A.personId;

