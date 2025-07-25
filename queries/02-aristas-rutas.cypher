UNWIND [
  {from: 'A', to: 'E', dist: 17.6}, {from: 'A', to: 'G', dist: 34.1},
  {from: 'A', to: 'K', dist: 52.8}, {from: 'A', to: 'C', dist: 16.5},
  {from: 'A', to: 'B', dist: 8.3},  {from: 'A', to: 'D', dist: 25.3},
  {from: 'A', to: 'F', dist: 70.4}, {from: 'A', to: 'P', dist: 89.7},
  {from: 'B', to: 'C', dist: 11.6},{from: 'B', to: 'F', dist: 68.8},
  {from: 'B', to: 'P', dist: 87.1},{from: 'B', to: 'D', dist: 31.5},
  {from: 'C', to: 'G', dist: 25.8},{from: 'C', to: 'H', dist: 45.0},
  {from: 'C', to: 'N', dist: 76.6},{from: 'D', to: 'J', dist: 47.4},
  {from: 'D', to: 'F', dist: 86.7},{from: 'D', to: 'P', dist: 110.0},
  {from: 'D', to: 'R', dist: 122.0},{from: 'E', to: 'I', dist: 22.1},
  {from: 'E', to: 'G', dist: 24.8},{from: 'E', to: 'K', dist: 43.2},
  {from: 'F', to: 'P', dist: 46.6},{from: 'F', to: 'Q', dist: 35.8},
  {from: 'G', to: 'H', dist: 22.3},{from: 'G', to: 'K', dist: 23.6},
  {from: 'G', to: 'N', dist: 77.7},{from: 'H', to: 'N', dist: 47.7},
  {from: 'H', to: 'O', dist: 70.5},{from: 'H', to: 'M', dist: 42.4},
  {from: 'H', to: 'W', dist: 110.0},{from: 'H', to: 'Y', dist: 151.0},
  {from: 'I', to: 'K', dist: 40.1},{from: 'J', to: 'Q', dist: 46.4},
  {from: 'J', to: 'V', dist: 105.0},{from: 'K', to: 'M', dist: 32.6},
  {from: 'K', to: 'L', dist: 46.1},{from: 'K', to: 'Y', dist: 147.0},
  {from: 'K', to: 'W', dist: 108.0},{from: 'L', to: 'S', dist: 64.6},
  {from: 'L', to: 'M', dist: 70.9},{from: 'M', to: 'Y', dist: 77.0},
  {from: 'M', to: 'W', dist: 86.0},{from: 'N', to: 'O', dist: 41.9},
  {from: 'N', to: 'P', dist: 54.6},{from: 'O', to: 'P', dist: 71.9},
  {from: 'O', to: 'W', dist: 84.4},{from: 'Q', to: 'V', dist: 59.2},
  {from: 'R', to: 'S', dist: 75.6},{from: 'R', to: 'T', dist: 54.2},
  {from: 'R', to: 'U', dist: 63.1},{from: 'S', to: 'T', dist: 62.4},
  {from: 'T', to: 'U', dist: 103.0},{from: 'W', to: 'X', dist: 50.1},
  {from: 'W', to: 'Y', dist: 85.2},{from: 'X', to: 'Z', dist: 73.9},
  {from: 'X', to: 'Y', dist: 76.7},{from: 'Y', to: 'Z', dist: 54.6}
] AS data
MATCH (a:Location {id: data.from}), (b:Location {id: data.to})
MERGE (a)-[r:CONNECTED]->(b)
SET r.distance = data.dist;