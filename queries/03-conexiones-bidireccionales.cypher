MATCH (a {id:'A'}), (l {id:'L'})
CREATE (a)-[:CONECTADO {distancia: 0.2}]->(l),
       (l)-[:CONECTADO {distancia: 0.2}]->(a);

MATCH (a {id:'A'}), (m {id:'M'})
CREATE (a)-[:CONECTADO {distancia: 2.3}]->(m),
       (m)-[:CONECTADO {distancia: 2.3}]->(a);

MATCH (b {id:'B'}), (i {id:'I'})
CREATE (b)-[:CONECTADO {distancia: 2.7}]->(i),
       (i)-[:CONECTADO {distancia: 2.7}]->(b);

MATCH (b {id:'B'}), (k {id:'K'})
CREATE (b)-[:CONECTADO {distancia: 3.5}]->(k),
       (k)-[:CONECTADO {distancia: 3.5}]->(b);

MATCH (c {id:'C'}), (n {id:'N'})
CREATE (c)-[:CONECTADO {distancia: 2.7}]->(n),
       (n)-[:CONECTADO {distancia: 2.7}]->(c);

MATCH (c {id:'C'}), (t {id:'T'})
CREATE (c)-[:CONECTADO {distancia: 3.3}]->(t),
       (t)-[:CONECTADO {distancia: 3.3}]->(c);

MATCH (d {id:'D'}), (e {id:'E'})
CREATE (d)-[:CONECTADO {distancia: 0.3}]->(e),
       (e)-[:CONECTADO {distancia: 0.3}]->(d);

MATCH (d {id:'D'}), (q {id:'Q'})
CREATE (d)-[:CONECTADO {distancia: 3.4}]->(q),
       (q)-[:CONECTADO {distancia: 3.4}]->(d);

MATCH (e {id:'E'}), (r {id:'R'})
CREATE (e)-[:CONECTADO {distancia: 3.6}]->(r),
       (r)-[:CONECTADO {distancia: 3.6}]->(e);

MATCH (e {id:'E'}), (y {id:'Y'})
CREATE (e)-[:CONECTADO {distancia: 1.3}]->(y),
       (y)-[:CONECTADO {distancia: 1.3}]->(e);

MATCH (f {id:'F'}), (y {id:'Y'})
CREATE (f)-[:CONECTADO {distancia: 2.1}]->(y),
       (y)-[:CONECTADO {distancia: 2.1}]->(f);

MATCH (f {id:'F'}), (z {id:'Z'})
CREATE (f)-[:CONECTADO {distancia: 0.7}]->(z),
       (z)-[:CONECTADO {distancia: 0.7}]->(f);

MATCH (g {id:'G'}), (s {id:'S'})
CREATE (g)-[:CONECTADO {distancia: 3.6}]->(s),
       (s)-[:CONECTADO {distancia: 3.6}]->(g);

MATCH (g {id:'G'}), (v {id:'V'})
CREATE (g)-[:CONECTADO {distancia: 1.0}]->(v),
       (v)-[:CONECTADO {distancia: 1.0}]->(g);

MATCH (h {id:'H'}), (u {id:'U'})
CREATE (h)-[:CONECTADO {distancia: 2.2}]->(u),
       (u)-[:CONECTADO {distancia: 2.2}]->(h);

MATCH (h {id:'H'}), (v {id:'V'})
CREATE (h)-[:CONECTADO {distancia: 3.6}]->(v),
       (v)-[:CONECTADO {distancia: 3.6}]->(h);

MATCH (i {id:'I'}), (j {id:'J'})
CREATE (i)-[:CONECTADO {distancia: 1.0}]->(j),
       (j)-[:CONECTADO {distancia: 1.0}]->(i);

MATCH (j {id:'J'}), (k {id:'K'})
CREATE (j)-[:CONECTADO {distancia: 0.7}]->(k),
       (k)-[:CONECTADO {distancia: 0.7}]->(j);

MATCH (j {id:'J'}), (m {id:'M'})
CREATE (j)-[:CONECTADO {distancia: 3.7}]->(m),
       (m)-[:CONECTADO {distancia: 3.7}]->(j);

MATCH (j {id:'J'}), (n {id:'N'})
CREATE (j)-[:CONECTADO {distancia: 3.2}]->(n),
       (n)-[:CONECTADO {distancia: 3.2}]->(j);

MATCH (l {id:'L'}), (n {id:'N'})
CREATE (l)-[:CONECTADO {distancia: 1.2}]->(n),
       (n)-[:CONECTADO {distancia: 1.2}]->(l);

MATCH (l {id:'L'}), (o {id:'O'})
CREATE (l)-[:CONECTADO {distancia: 2.7}]->(o),
       (o)-[:CONECTADO {distancia: 2.7}]->(l);

MATCH (m {id:'M'}), (t {id:'T'})
CREATE (m)-[:CONECTADO {distancia: 0.5}]->(t),
       (t)-[:CONECTADO {distancia: 0.5}]->(m);

MATCH (n {id:'N'}), (t {id:'T'})
CREATE (n)-[:CONECTADO {distancia: 3.8}]->(t),
       (t)-[:CONECTADO {distancia: 3.8}]->(n);

MATCH (o {id:'O'}), (u {id:'U'})
CREATE (o)-[:CONECTADO {distancia: 3.1}]->(u),
       (u)-[:CONECTADO {distancia: 3.1}]->(o);

MATCH (o {id:'O'}), (p {id:'P'})
CREATE (o)-[:CONECTADO {distancia: 3.3}]->(p),
       (p)-[:CONECTADO {distancia: 3.3}]->(o);

MATCH (p {id:'P'}), (q {id:'Q'})
CREATE (p)-[:CONECTADO {distancia: 2.8}]->(q),
       (q)-[:CONECTADO {distancia: 2.8}]->(p);

MATCH (p {id:'P'}), (s {id:'S'})
CREATE (p)-[:CONECTADO {distancia: 3.8}]->(s),
       (s)-[:CONECTADO {distancia: 3.8}]->(p);

MATCH (q {id:'Q'}), (r {id:'R'})
CREATE (q)-[:CONECTADO {distancia: 2.1}]->(r),
       (r)-[:CONECTADO {distancia: 2.1}]->(q);

MATCH (r {id:'R'}), (s {id:'S'})
CREATE (r)-[:CONECTADO {distancia: 0.9}]->(s),
       (s)-[:CONECTADO {distancia: 0.9}]->(r);

MATCH (r {id:'R'}), (w {id:'W'})
CREATE (r)-[:CONECTADO {distancia: 3.2}]->(w),
       (w)-[:CONECTADO {distancia: 3.2}]->(r);

MATCH (t {id:'T'}), (u {id:'U'})
CREATE (t)-[:CONECTADO {distancia: 3.9}]->(u),
       (u)-[:CONECTADO {distancia: 3.9}]->(t);

MATCH (v {id:'V'}), (w {id:'W'})
CREATE (v)-[:CONECTADO {distancia: 0.6}]->(w),
       (w)-[:CONECTADO {distancia: 0.6}]->(v);

MATCH (v {id:'V'}), (x {id:'X'})
CREATE (v)-[:CONECTADO {distancia: 1.7}]->(x),
       (x)-[:CONECTADO {distancia: 1.7}]->(v);

MATCH (w {id:'W'}), (y {id:'Y'})
CREATE (w)-[:CONECTADO {distancia: 2.0}]->(y),
       (y)-[:CONECTADO {distancia: 2.0}]->(w);

MATCH (w {id:'W'}), (x {id:'X'})
CREATE (w)-[:CONECTADO {distancia: 1.9}]->(x),
       (x)-[:CONECTADO {distancia: 1.9}]->(w);

MATCH (x {id:'X'}), (z {id:'Z'})
CREATE (x)-[:CONECTADO {distancia: 2.8}]->(z),
       (z)-[:CONECTADO {distancia: 2.8}]->(x);