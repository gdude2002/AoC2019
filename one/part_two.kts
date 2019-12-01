import java.io.File
import kotlin.math.floor

fun getFuel(mass: Float) : Float {
    return floor(mass / 3) - 2
}

fun getRealTotal(fuel: Float) : Float {
    val additional = getFuel(fuel)

    if (additional <= 0) {
        return fuel
    }

    return fuel + getRealTotal(additional)
}

fun main() {
    var total = 0f

    File("data.txt").forEachLine {
        total += getRealTotal(getFuel(it.toFloat()))
    }

    print("Total: ${total.toInt()}")
}

main()
