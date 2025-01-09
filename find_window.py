import pygetwindow as gw

def list_all_window_titles():
    windows = gw.getAllWindows()
    titles = [win.title for win in windows if win.title]
    return titles

if __name__ == "__main__":
    titles = list_all_window_titles()
    print("Active window titles:")
    for title in titles:
        print(title)
