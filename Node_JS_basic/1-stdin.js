process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.once('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
  process.stdout.write('This important software is now closing\n');
  process.exit();
});
