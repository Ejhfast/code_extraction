# Running Python script calling packages in terminal
package = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(package)
