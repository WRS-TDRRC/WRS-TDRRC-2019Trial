import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "RTM")
