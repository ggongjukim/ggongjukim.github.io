const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input.push(line);
  if(input.length > 2) rl.close();
}).on('close', function () {
  //console.log(input);
  let [num, DNA, rule] = input;
  //console.log(input);
  let p = Number(num.split(' ')[1]);
  let [a, c, g, t] = rule.split(' ');
  a = Number(a);
  c = Number(c);
  g = Number(g);
  t = Number(t);
  //console.log(a, c, g, t);
  let [start, end] = [0, p];
  let count = 0;

  while (end <= DNA.length) {
    let result = {
      A: 0,
      C: 0,
      G: 0,
      T: 0,
    };
    let temp = DNA.slice(start, end).split('');
    //console.log('temp', temp);
    temp.map((i) => {
      result[i] += 1;
    });
    if (result.A < a || result.C < c || result.G < g || result.T < t) {
      start += 1;
      end += 1;
    } else {
      count += 1;
      start += 1;
      end += 1;
    }
  }
  console.log(count);
  process.exit();
});
