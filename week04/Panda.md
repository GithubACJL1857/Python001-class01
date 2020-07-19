> 假定panda为pandas的DataFrame对象。

#### 1. SELECT * FROM data;
 `panda` 

#### 2. SELECT * FROM data LIMIT(10);
 `panda.head(10)` 

#### 3. SELECT id FROM data;  //id 是 data 表的特定一列
 `panda['id']`
 `panda.id`


#### 4. SELECT COUNT(id) FROM data;
 `panda['id'].shape[0]`

#### 5. SELECT * FROM data WHERE id<1000 AND age>30;
 `panda[(panda['id'] < 1000) & (panda['age'] > 30)]`

#### 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
 `panda.groupby('id').order_id.nunique()`

#### 7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
 `pd.merge(table1, table2, on='id')`

#### 8. SELECT * FROM table1 UNION SELECT * FROM table2;
 `pd.concat([table1, table2]).drop_duplicates()`

#### 9. DELETE FROM table1 WHERE id=10;
`indexname = panda[panda['id'] == 10].index`
`panda.drop(indexname, inplace=True)`

#### 10. ALTER TABLE table1 DROP COLUMN column_name;
`panda.drop(['B'], axis=1)`
`panda.drop(columns=['B'])`
