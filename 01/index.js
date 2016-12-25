fs = require('fs')

NORTH=0
EAST=1
SOUTH=2
WEST=3

function nextDirection(cur, turn) {
  if (turn == 'R') { return (cur + 1) % 4; }
  else if (cur == 0) { return 3; }
  else { return cur - 1; }
}

function processToken(token) {
  return {
    turn: token[0],
    dist: parseInt(token.substring(1))
  }
}

function updateLocation(payload) {
  for (j=payload.dist; j > 0; j--) {
    if (payload.facing == NORTH) {
      payload.y += 1
    } else if (payload.facing == SOUTH) {
      payload.y -= 1
    } else if (payload.facing == EAST) {
      payload.x += 1
    } else if (payload.facing == WEST) {
      payload.x -= 1
    } else {
      console.log("INVALID DIRECTION.")
    }

    key = payload.x + " " + payload.y

    if (!(key in payload.locations)) {
      payload.locations[key] = 0;
    }

    payload.locations[key] = payload.locations[key]+1
    if (!payload.foundHq && payload.locations[key] > 1) {
      payload.foundHq = true
      payload.HQ = Math.abs(payload.x) + Math.abs(payload.y)
    }
  }
}

fs.readFile('input.txt', 'utf8', function (err,input) {
  if (err) {
    return console.log(err)
  }

  data = {
    facing : NORTH,
    locations : {},
    y : 0,
    x : 0,
    dist : 0,
    foundHq : false
  }

  data.locations["0_0"] = 1

  var tokens = input.trim().split(", ")
  for (i = 0; i < tokens.length; i++) {
    token = processToken(tokens[i])
    data.facing = nextDirection(data.facing, token.turn)
    data.dist = token.dist
    updateLocation(data)
  }

  console.log("Blocks away Q1: " + (Math.abs(data.y) + Math.abs(data.x)))
  console.log("Blocks away Q2: " + data.HQ)
})
