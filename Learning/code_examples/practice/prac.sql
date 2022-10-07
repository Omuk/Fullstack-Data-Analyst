CREATE DATABASE Mydatabase;

CREATE TABLE MyTable(
    PersonID int,
    Names VARCHAR(100),
    City VARCHAR(100)
    ToDrop VARCHAR(100)
);

CREATE INDEX MyTableIndex
ON MyTable(PersonID, Names, City);

INSERT INTO MyTable
VALUES (
    '6568', 'Jesse, James', 'San Diego'
    '8574', 'Michael, Echo', 'Los Anges',
    '8573', 'Poko,Paka', 'San Francisco',
);

ALTER TABLE MyTable
DROP COLUMN VARCHAR;

ALTER TABLE MyTable
ADD State VARCHAR(100);

Select PersonID
FROM Mytable 
WHERE PersonID=6568
GROUP BY 
HAVING
ORDER BY

SELECT MyTable.PersonID, MyTable.Names
FROM MyTable LEFT JOIN MyTable2 ON MyTable.PersonID = MyTable2.PersonID

SELECT Table1.column1, Table2.Column2,
FROM Table1 LEFT JOIN Table2 on Table1.column1 = Table2.coulmn2


