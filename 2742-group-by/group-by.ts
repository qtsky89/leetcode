interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}


Array.prototype.groupBy = function<T>(fn: (item:T) => string ) {
    const ret: Record<string, T[]> = {}

    for (const item of this) {
        const key = fn(item)

        if (key in ret) {
            ret[key].push(item)
        } else {
            ret[key] = [item]
        }
    }
    return ret
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */