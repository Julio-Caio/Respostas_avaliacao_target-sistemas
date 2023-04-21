const readLine = require('readline')

const stringsReversed = []


const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Type a string: ', (answer) => {
    const string = answer;
    const stringArray = string.split('');

for (let i = stringArray.length - 1; i >=0; i--) {
    stringsReversed.push(stringArray[i])
}

const stringReversed = stringsReversed.join('')

console.log(stringReversed);
rl.close();

})