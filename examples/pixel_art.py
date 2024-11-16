import pixray
pixray.reset_settings()
pixray.add_settings(prompts="Rainbow paint brush",
                    drawer="pixel",
                    aspect="square",
                    outdir="outputs/pyxgen_logo_v2",
                    iterations=200,
                    learning_rate_drops=[20, 70, 95],
                    gamma_lr=0.1,
                    num_cuts=2,
                    batches=5,
                    custom_loss="smoothness:0.5, aesthetic:0.3",
                    pixel_size=(32, 32))
settings = pixray.apply_settings()
pixray.do_init(settings)
pixray.do_run(settings)

# TODO: understand the different drawers
# TODO: understand the quality parameter => Seems to load different CLIP models. It also specifies things like scale, num_cuts, num_batches, etc... unless they
#  are explicitly set. It's like a high-level parameter.
# TODO: understand the num_cuts parameter => Reduces the required VRAM (I guess the required VRAM for some model is proportional to num_cuts, but you have multiple
#  model (for encoding text, encoding image, generating image) so the effect of dividing by 10 the num_cuts is not a reduction by 10 of the required VRAM.
#  Similarly for the computation time. Default is 30, but using like 20 reduces the risk of CUDA memory error.
#  CLIP can only process patches of 224x224 so the typical way of evolving an image involves making a batch random crops at different scales so it can work on the whole
#  image as well as details at the same time. To understand it better, need to look at MakeCutouts (although the code is super hard to understand).
# TODO: understand batches: I think it's not a batch size, so it's just slowing things down to use several batches. Maybe it makes just 1 update after seing
#  `batches` batches. It does not use more memory to increase batches.
