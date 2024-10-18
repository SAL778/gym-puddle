from gymnasium.envs.registration import register

register(
    id='PuddleWorld-v0',
    entry_point='gym_puddle.env.puddle_env:PuddleEnv',
)
