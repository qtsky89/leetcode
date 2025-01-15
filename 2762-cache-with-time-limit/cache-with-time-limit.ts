type MapEntry = { value: number, timeout: NodeJS.Timeout }

class TimeLimitedCache {
    cache = new Map<number, MapEntry>()
    
    set(key: number, value: number, duration: number): boolean {
        const valueInCache = this.cache.get(key)

        if (valueInCache) {
            clearTimeout(valueInCache.timeout)
        }
        const timeout = setTimeout(() => this.cache.delete(key), duration)
        this.cache.set(key, {value, timeout})
        return Boolean(valueInCache)
    }
    
    get(key: number): number {
        return this.cache.has(key) ? this.cache.get(key).value : -1
    }
    
    count(): number {
        return this.cache.size
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */