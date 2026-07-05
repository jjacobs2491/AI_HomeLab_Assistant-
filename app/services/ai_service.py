from app.services.system_service import get_system_info


def ask_ai(question: str):
    system = get_system_info()

    return {
        "question": question,
        "response": (
            f"System status check complete. "
            f"CPU usage is {system['cpu_usage']}%, "
            f"memory usage is {system['memory_usage']}%, "
            f"and disk usage is {system['disk_usage']}%."
        )
    }