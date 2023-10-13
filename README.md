# SparseAttention

[AttentionCtx](https://github.com/krosac/SparseAttention/blob/master/diffusers/src/diffusers/models/attention_ctx.py) collects metrics during the computation of [AttnProcessor](https://github.com/krosac/SparseAttention/blob/master/diffusers/src/diffusers/models/attention_processor.py#L542)


## Run
build environment with docker
```
cd docker-gpu
sh build.sh attn-gpu
sh run.sh $(pwd)/.. attn-gpu
```
install custom diffusers package
```
sh install.sh
```
generate image
```
python main.py
```
