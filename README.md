# Net Return Surface Plot Model

Enter score, risk, and odds for 4 wagers: over, under, favorite, dog.<br>
Calculate net-result for 144 total point / spread pairings (12x12).<br>
Display 3D surface plots with spread(x-axis), total-points(y-axis), and net-result(z-axis).<br>


requirements
-
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Mpl_toolkits.mplot3d](https://matplotlib.org/3.2.1/api/toolkits/mplot3d.html)



nr_input.py
-

- Define lambda function 'g' for calculating 'win' for each wager.<br>
- Enter input variables (score/odds/risk) for each wager.<br>
- Create variables to define ranges for total point / spread axis'.<br>
- Calculate 'win' values with lambda function 'g'.<br>
- Create spr/tp variables, then scenario variables, append scenario var to scenario lists.<br>
- Create scenario matrix DataFrame, create scenario breakdown DataFrame.<br>

nr_results.py
-

- Import nr_input, Create spread and total point DataFrames, add step 1c range variables to each df.<br>
- Create lists of monetary results for each wager.<br>
- Define nr_result() function:<br>

	- Add lists from step 2b to df's from step 2a, calculate net-spread and net-total-points.<br>
	- Create simple lists of net-spread / net-total-point values.<br>
	- Define 'net_map' variable with global scope<br>
	- Create 12 x 12 Numpy array of net-result (net_map).<br>

- Define decorator function that calls nr_result() and nrvisual()<br>

- Define nr_visual() function:<br>
	- Import matplotlib and mpl_toolkit, create matplotlib figure, add 4 subplots displayed 2x2.<br>
	- Create 'x' and 'y' variables; assign values from range variables (spr_pts/tp_pts) to 'x' and 'y'.<br>
	- Use 'x' and 'y' to create Numpy meshgrid 'X, Y'. Assign net_map to 'Z'.<br>
	- Create colormap 'mycmap'. For each axis: add titles and create surf-plot.<br>
	- Assign view angle to each axis using 'view_init(elevation, azimuth)'<br>
	- Display matplotlib figure with 'plt.show()'<br>

- Call nrvisual()

nr_execute.py
-

- Import DataFrames from nr_input, Import surf-plot function from nr_results
- Define scn_stats() function:
	- print both df imported from nr_input
- Define decorator function that calls scn_stats() and surf4()

- Define surf4() function:
	- call nrvisual()

- Display risk / win / score for each wager

<br>
<br>

Visit [Abovetb.com](https://www.abovetb.com/)
-
