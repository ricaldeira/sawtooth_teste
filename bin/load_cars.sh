#!/bin/bash
set -B
export JWT=eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4ODcwMTU1OCwiZXhwIjoxNTg4NzA1MTU4fQ.eyJwdWJsaWNfa2V5IjoiMDJlMTIzOTM5NjQ3ZjJjODRkNzc1ZmM0ZmE2YmQ5OGE4ZWQzZjkyOWFiYWUyNzRiYjlhODYxYWE3OTJiZThkNTAyIn0.pFwyBDH3PnKw7sSxwlPgsU-zhhhRgNJQWtvO5Oh5EvARDam1YidjNkEuSOnx0xqixouJCMDg-5jHxA9xHRA_vw

for i in {1..10}; do
    curl -X POST -d '{"chassis":"50550-0840844-41098409-461065400'$i'", "license":"AMM-0222'$i'"}' -H 'Authorization: Bearer '$JWT http://localhost:8000/cars
done