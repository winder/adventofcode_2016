use std::io;
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

const NORTH: i32 = 1;
const EAST: i32 = 2;
const SOUTH: i32 = 3;
const WEST: i32 = 4;

fn next_dir(cur: i32, turn: char) -> i32 {
  if turn == 'R'{ return (cur+1)%4; }
  else if cur == 1{ return 4; }
  else{ return cur-1; }
}

fn main() {
  let fileStr = get_file_as_string();
  println! ("File: {}", fileStr);
  let tokens = fileStr.split(",");

  let mut facing = NORTH;
  let mut dist_ns = 0;
  let mut dist_ew = 0;

  for token in tokens {
      let mut char_iter = token.chars();
      let first = char_iter.next();
      let dir = char_iter.next().unwrap();
      let dist = char_iter.next().unwrap();
      println!("'{}' {} -> {}", token, dir, dist);
  }
}

fn get_file_as_string() -> String {
  // Create a path to the desired file
  let path = Path::new("input.txt");
  let display = path.display();
  println!("Path display: {}", display);
  // Open the path in read-only mode, returns `io::Result<File>`
  let mut file = match File::open(&path) {
    // The `description` method of `io::Error` returns a string that describes the error
    Err(why) => panic!("couldn't open {}: {}", display, why.description()),
    Ok(file) => file,
  };

  // Read the file contents into a string, returns `io::Result<usize>`
  let mut s = String::new();
  match file.read_to_string(&mut s) {
    Err(why) => panic!("couldn't read {}: {}", display, why.description()),
    Ok(_) => print!("{} contains:\n{}", display, s),
  }

  return s;
}

