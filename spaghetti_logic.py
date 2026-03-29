from typing import Callable, Iterable, List


TAX_RATE = 1.15
DEFAULT_LOG_FILE = "log.txt"


def apply_tax(value: float, tax_rate: float = TAX_RATE) -> float:
    """Return value after tax multiplier is applied."""
    return value * tax_rate


def format_total_line(total: float) -> str:
    """Format output line for a computed total."""
    return f"Total: {total:.2f}"


def write_results_log(results: List[float], log_file: str = DEFAULT_LOG_FILE) -> None:
    """Append processed results to a log file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{results}\n")


def process_data(
    data: Iterable[float],
    tax_rate: float = TAX_RATE,
    output: Callable[[str], None] = print,
    log_file: str = DEFAULT_LOG_FILE,
) -> List[float]:
    """Process numeric values by applying tax, printing totals, and logging results."""
    results: List[float] = []

    for item in data:
        total = apply_tax(float(item), tax_rate)
        output(format_total_line(total))
        results.append(total)

    write_results_log(results, log_file)
    return results
