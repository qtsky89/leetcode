type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let x = init;

    return {
        increment: () => {
            x++;
            return x;
        },
        decrement: () =>  {
            x--;
            return x;
        },
        reset: () => {
            x = init;
            return x;
        }
    } 
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */