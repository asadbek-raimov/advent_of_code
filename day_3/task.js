const fs = require("fs")

function arrange() {
    const buffer = fs.readFileSync("./day_3/input.txt")
    const list = String(buffer).split("\n")
    let resSum = 0;

    for (const bat of list) {
        let maxIndex = 0;
        for (let i = maxIndex + 1; i < bat.length - 1; i++) {
            if (bat[maxIndex] < bat[i]) {
                maxIndex = i
            }
        }

        let secondMaxIndex = maxIndex + 1;
        for (let j = secondMaxIndex; j < bat.length; j++) {
            if (bat[secondMaxIndex] < bat[j]) {
                secondMaxIndex = j
            }
        }

        let current = Number(bat[maxIndex] + bat[secondMaxIndex])
        resSum += current
    }


    return resSum
}

function gather() {
    const buffer = fs.readFileSync("./day_3/input.txt")
    const list = String(buffer).split("\n")
    const res = []

    for (let bat of list) {
        const max_digits =[]
        let maxIdx = 0
        for (let need = 11; need >= 0; need--) {
            for (let i = maxIdx; i < bat.length - need; i++) {
                if (+bat[maxIdx] < +bat[i]) {
                    maxIdx = i
                }
            }
            max_digits.push(bat[maxIdx])
            console.log(max_digits)
            maxIdx += 1
        }
        res.push(+max_digits.join(""))
    }

    return res.reduce((acc, curr) => acc + curr , 0)
}


console.log(
    gather());
