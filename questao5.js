const readLine = require('readline')

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Type a string: ', (answer) => {
    const string = answer;
    const stringArray = string.split('');
    const stringArrayReversed = stringArray.reverse();
    const stringReversed = stringArrayReversed.join('');
    console.log(stringReversed);
    rl.close();
})