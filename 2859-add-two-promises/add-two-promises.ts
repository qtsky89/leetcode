type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    let ret = await Promise.all([promise1, promise2])

    let sumVal = 0;

    for(let i=0; i < ret.length; i++) {
        sumVal += ret[i]
    }

    return sumVal;
    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */