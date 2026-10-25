.class public final Lfk;
.super Ljava/lang/Object;
.source "r8-map-id-290ebb60cd1ac122145cca66461ed9e7d2f764a7712c78a8a3c838fecaf4f98f"

# interfaces
.implements Lac1;
.implements Lcm4;


# instance fields
.field public f:Landroid/content/Context;


# direct methods
.method public synthetic constructor <init>(Landroid/content/Context;B)V
    .locals 0

    .line 25
    iput-object p1, p0, Lfk;->f:Landroid/content/Context;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;I)V
    .locals 0

    .line 1
    packed-switch p2, :pswitch_data_0

    .line 2
    .line 3
    .line 4
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 5
    .line 6
    .line 7
    invoke-virtual {p1}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    .line 8
    .line 9
    .line 10
    move-result-object p1

    .line 11
    iput-object p1, p0, Lfk;->f:Landroid/content/Context;

    .line 12
    .line 13
    return-void

    .line 14
    :pswitch_0
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 15
    .line 16
    .line 17
    invoke-virtual {p1}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    .line 18
    .line 19
    .line 20
    move-result-object p1

    .line 21
    iput-object p1, p0, Lfk;->f:Landroid/content/Context;

    .line 22
    .line 23
    return-void

    .line 24
    nop

    .line 25
    :pswitch_data_0
    .packed-switch 0x3
        :pswitch_0
    .end packed-switch
.end method

.method public static e(Lg80;Leg;Ljava/time/Instant;FZLnz0;)V
    .locals 23

    .line 1
    move-object/from16 v0, p1

    .line 2
    .line 3
    move-object/from16 v1, p2

    .line 4
    .line 5
    move-object/from16 v2, p5

    .line 6
    .line 7
    iget v2, v2, Lnz0;->f:F

    .line 8
    .line 9
    iget-object v3, v0, Leg;->c:Ljava/time/Instant;

    .line 10
    .line 11
    iget v4, v0, Leg;->d:F

    .line 12
    .line 13
    float-to-long v4, v4

    .line 14
    invoke-virtual {v3, v4, v5}, Ljava/time/Instant;->plusSeconds(J)Ljava/time/Instant;

    .line 15
    .line 16
    .line 17
    move-result-object v3

    .line 18
    iget-object v0, v0, Leg;->c:Ljava/time/Instant;

    .line 19
    .line 20
    invoke-virtual {v0, v1}, Ljava/time/Instant;->isBefore(Ljava/time/Instant;)Z

    .line 21
    .line 22
    .line 23
    move-result v4

    .line 24
    if-eqz v4, :cond_3

    .line 25
    .line 26
    invoke-virtual {v3, v1}, Ljava/time/Instant;->isAfter(Ljava/time/Instant;)Z

    .line 27
    .line 28
    .line 29
    move-result v3

    .line 30
    if-nez v3, :cond_0

    .line 31
    .line 32
    goto/16 :goto_3

    .line 33
    .line 34
    :cond_0
    invoke-static {v0, v1}, Ljava/time/Duration;->between(Ljava/time/temporal/Temporal;Ljava/time/temporal/Temporal;)Ljava/time/Duration;

    .line 35
    .line 36
    .line 37
    move-result-object v0

    .line 38
    invoke-virtual {v0}, Ljava/time/Duration;->getSeconds()J

    .line 39
    .line 40
    .line 41
    move-result-wide v0

    .line 42
    long-to-float v0, v0

    .line 43
    mul-float v0, v0, p3

    .line 44
    .line 45
    if-eqz p4, :cond_1

    .line 46
    .line 47
    sget-wide v3, Loe0;->f:J

    .line 48
    .line 49
    :goto_0
    move-wide v6, v3

    .line 50
    goto :goto_1

    .line 51
    :cond_1
    sget-wide v3, Loe0;->b:J

    .line 52
    .line 53
    goto :goto_0

    .line 54
    :goto_1
    if-eqz p4, :cond_2

    .line 55
    .line 56
    const/high16 v1, -0x1000000

    .line 57
    .line 58
    goto :goto_2

    .line 59
    :cond_2
    const/4 v1, -0x1

    .line 60
    :goto_2
    invoke-interface/range {p0 .. p0}, Lb61;->c()J

    .line 61
    .line 62
    .line 63
    move-result-wide v3

    .line 64
    const-wide v16, 0xffffffffL

    .line 65
    .line 66
    .line 67
    .line 68
    .line 69
    and-long v3, v3, v16

    .line 70
    .line 71
    long-to-int v3, v3

    .line 72
    invoke-static {v3}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 73
    .line 74
    .line 75
    move-result v3

    .line 76
    invoke-static {v0}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 77
    .line 78
    .line 79
    move-result v4

    .line 80
    int-to-long v4, v4

    .line 81
    invoke-static {v3}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 82
    .line 83
    .line 84
    move-result v3

    .line 85
    int-to-long v8, v3

    .line 86
    const/16 v3, 0x20

    .line 87
    .line 88
    shl-long/2addr v4, v3

    .line 89
    and-long v8, v8, v16

    .line 90
    .line 91
    or-long/2addr v8, v4

    .line 92
    invoke-static {v0}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 93
    .line 94
    .line 95
    move-result v4

    .line 96
    int-to-long v4, v4

    .line 97
    const/16 v18, 0x0

    .line 98
    .line 99
    invoke-static/range {v18 .. v18}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 100
    .line 101
    .line 102
    move-result v10

    .line 103
    int-to-long v10, v10

    .line 104
    shl-long/2addr v4, v3

    .line 105
    and-long v10, v10, v16

    .line 106
    .line 107
    or-long/2addr v10, v4

    .line 108
    const/high16 v4, 0x40800000    # 4.0f

    .line 109
    .line 110
    mul-float v12, v2, v4

    .line 111
    .line 112
    const/4 v14, 0x0

    .line 113
    const/16 v15, 0x1f0

    .line 114
    .line 115
    const/4 v13, 0x0

    .line 116
    move-object/from16 v5, p0

    .line 117
    .line 118
    invoke-static/range {v5 .. v15}, Lb61;->q0(Lb61;JJJFILil;I)V

    .line 119
    .line 120
    .line 121
    new-instance v4, Landroid/graphics/Paint;

    .line 122
    .line 123
    const/4 v5, 0x1

    .line 124
    invoke-direct {v4, v5}, Landroid/graphics/Paint;-><init>(I)V

    .line 125
    .line 126
    .line 127
    invoke-virtual {v4, v1}, Landroid/graphics/Paint;->setColor(I)V

    .line 128
    .line 129
    .line 130
    sget-object v1, Landroid/graphics/Paint$Align;->CENTER:Landroid/graphics/Paint$Align;

    .line 131
    .line 132
    invoke-virtual {v4, v1}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V

    .line 133
    .line 134
    .line 135
    const/high16 v1, 0x41400000    # 12.0f

    .line 136
    .line 137
    mul-float/2addr v1, v2

    .line 138
    invoke-virtual {v4, v1}, Landroid/graphics/Paint;->setTextSize(F)V

    .line 139
    .line 140
    .line 141
    invoke-virtual {v4, v5}, Landroid/graphics/Paint;->setFakeBoldText(Z)V

    .line 142
    .line 143
    .line 144
    new-instance v1, Landroid/graphics/Rect;

    .line 145
    .line 146
    invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V

    .line 147
    .line 148
    .line 149
    const/4 v5, 0x0

    .line 150
    const/4 v8, 0x2

    .line 151
    const-string v9, "\uc9c0\uae08"

    .line 152
    .line 153
    invoke-virtual {v4, v9, v5, v8, v1}, Landroid/graphics/Paint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V

    .line 154
    .line 155
    .line 156
    const/high16 v5, 0x41000000    # 8.0f

    .line 157
    .line 158
    mul-float v8, v2, v5

    .line 159
    .line 160
    const/high16 v10, 0x40a00000    # 5.0f

    .line 161
    .line 162
    mul-float/2addr v10, v2

    .line 163
    invoke-virtual {v1}, Landroid/graphics/Rect;->width()I

    .line 164
    .line 165
    .line 166
    move-result v11

    .line 167
    int-to-float v11, v11

    .line 168
    const/high16 v19, 0x40000000    # 2.0f

    .line 169
    .line 170
    mul-float v8, v8, v19

    .line 171
    .line 172
    add-float/2addr v8, v11

    .line 173
    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    .line 174
    .line 175
    .line 176
    move-result v11

    .line 177
    int-to-float v11, v11

    .line 178
    mul-float v10, v10, v19

    .line 179
    .line 180
    add-float v20, v10, v11

    .line 181
    .line 182
    invoke-interface/range {p0 .. p0}, Lb61;->c()J

    .line 183
    .line 184
    .line 185
    move-result-wide v10

    .line 186
    shr-long/2addr v10, v3

    .line 187
    long-to-int v10, v10

    .line 188
    invoke-static {v10}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 189
    .line 190
    .line 191
    move-result v10

    .line 192
    invoke-static {v0, v8, v10}, Lr43;->x(FFF)F

    .line 193
    .line 194
    .line 195
    move-result v0

    .line 196
    invoke-static {v0}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 197
    .line 198
    .line 199
    move-result v10

    .line 200
    int-to-long v10, v10

    .line 201
    invoke-static/range {v18 .. v18}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 202
    .line 203
    .line 204
    move-result v12

    .line 205
    int-to-long v12, v12

    .line 206
    shl-long/2addr v10, v3

    .line 207
    and-long v12, v12, v16

    .line 208
    .line 209
    or-long/2addr v10, v12

    .line 210
    invoke-static {v8}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 211
    .line 212
    .line 213
    move-result v12

    .line 214
    int-to-long v12, v12

    .line 215
    invoke-static/range {v20 .. v20}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 216
    .line 217
    .line 218
    move-result v14

    .line 219
    int-to-long v14, v14

    .line 220
    shl-long/2addr v12, v3

    .line 221
    and-long v14, v14, v16

    .line 222
    .line 223
    or-long/2addr v12, v14

    .line 224
    mul-float v14, v2, v5

    .line 225
    .line 226
    mul-float/2addr v2, v5

    .line 227
    invoke-static {v14}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 228
    .line 229
    .line 230
    move-result v5

    .line 231
    int-to-long v14, v5

    .line 232
    invoke-static {v2}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 233
    .line 234
    .line 235
    move-result v2

    .line 236
    move/from16 p1, v3

    .line 237
    .line 238
    move-object/from16 p2, v4

    .line 239
    .line 240
    int-to-long v3, v2

    .line 241
    shl-long v14, v14, p1

    .line 242
    .line 243
    and-long v2, v3, v16

    .line 244
    .line 245
    or-long/2addr v2, v14

    .line 246
    const/4 v14, 0x0

    .line 247
    const/16 v15, 0xf0

    .line 248
    .line 249
    move-object/from16 v5, p0

    .line 250
    .line 251
    move-wide/from16 v21, v2

    .line 252
    .line 253
    move v2, v8

    .line 254
    move-object v3, v9

    .line 255
    move-wide v8, v10

    .line 256
    move-wide v10, v12

    .line 257
    move-wide/from16 v12, v21

    .line 258
    .line 259
    invoke-static/range {v5 .. v15}, Lb61;->W(Lb61;JJJJLc61;I)V

    .line 260
    .line 261
    .line 262
    iget-object v4, v5, Lg80;->g:Ler;

    .line 263
    .line 264
    invoke-virtual {v4}, Ler;->v()Le80;

    .line 265
    .line 266
    .line 267
    move-result-object v4

    .line 268
    invoke-static {v4}, Lkh;->a(Le80;)Landroid/graphics/Canvas;

    .line 269
    .line 270
    .line 271
    move-result-object v4

    .line 272
    div-float v8, v2, v19

    .line 273
    .line 274
    add-float/2addr v8, v0

    .line 275
    div-float v20, v20, v19

    .line 276
    .line 277
    add-float v20, v20, v18

    .line 278
    .line 279
    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    .line 280
    .line 281
    .line 282
    move-result v0

    .line 283
    div-int/lit8 v0, v0, 0x2

    .line 284
    .line 285
    int-to-float v0, v0

    .line 286
    add-float v20, v20, v0

    .line 287
    .line 288
    iget v0, v1, Landroid/graphics/Rect;->bottom:I

    .line 289
    .line 290
    int-to-float v0, v0

    .line 291
    sub-float v0, v20, v0

    .line 292
    .line 293
    move-object/from16 v1, p2

    .line 294
    .line 295
    invoke-virtual {v4, v3, v8, v0, v1}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    .line 296
    .line 297
    .line 298
    :cond_3
    :goto_3
    return-void
.end method


# virtual methods
.method public a(Lp60;)V
    .locals 8

    .line 1
    new-instance v7, Lll0;

    .line 2
    .line 3
    const-string v0, "EmojiCompatInitializer"

    .line 4
    .line 5
    invoke-direct {v7, v0}, Lll0;-><init>(Ljava/lang/String;)V

    .line 6
    .line 7
    .line 8
    new-instance v0, Ljava/util/concurrent/ThreadPoolExecutor;

    .line 9
    .line 10
    new-instance v6, Ljava/util/concurrent/LinkedBlockingDeque;

    .line 11
    .line 12
    invoke-direct {v6}, Ljava/util/concurrent/LinkedBlockingDeque;-><init>()V

    .line 13
    .line 14
    .line 15
    const/4 v1, 0x0

    .line 16
    const/4 v2, 0x1

    .line 17
    const-wide/16 v3, 0xf

    .line 18
    .line 19
    sget-object v5, Ljava/util/concurrent/TimeUnit;->SECONDS:Ljava/util/concurrent/TimeUnit;

    .line 20
    .line 21
    invoke-direct/range {v0 .. v7}, Ljava/util/concurrent/ThreadPoolExecutor;-><init>(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/ThreadFactory;)V

    .line 22
    .line 23
    .line 24
    const/4 v1, 0x1

    .line 25
    invoke-virtual {v0, v1}, Ljava/util/concurrent/ThreadPoolExecutor;->allowCoreThreadTimeOut(Z)V

    .line 26
    .line 27
    .line 28
    new-instance v1, Ltm;

    .line 29
    .line 30
    const/4 v2, 0x2

    .line 31
    invoke-direct {v1, p0, p1, v0, v2}, Ltm;-><init>(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)V

    .line 32
    .line 33
    .line 34
    invoke-virtual {v0, v1}, Ljava/util/concurrent/ThreadPoolExecutor;->execute(Ljava/lang/Runnable;)V

    .line 35
    .line 36
    .line 37
    return-void
.end method

.method public b(Ll11;)Ldm4;
    .locals 3

    .line 1
    iget-object p0, p0, Lfk;->f:Landroid/content/Context;

    .line 2
    .line 3
    iget-object v0, p1, Ll11;->c:Ljava/lang/Object;

    .line 4
    .line 5
    check-cast v0, Ljava/lang/String;

    .line 6
    .line 7
    iget-object p1, p1, Ll11;->d:Ljava/lang/Object;

    .line 8
    .line 9
    check-cast p1, Lbm4;

    .line 10
    .line 11
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 12
    .line 13
    .line 14
    if-eqz v0, :cond_0

    .line 15
    .line 16
    invoke-virtual {v0}, Ljava/lang/String;->length()I

    .line 17
    .line 18
    .line 19
    move-result v1

    .line 20
    if-eqz v1, :cond_0

    .line 21
    .line 22
    new-instance v1, Ll11;

    .line 23
    .line 24
    const/4 v2, 0x1

    .line 25
    invoke-direct {v1, p0, v0, p1, v2}, Ll11;-><init>(Landroid/content/Context;Ljava/lang/String;Lbm4;Z)V

    .line 26
    .line 27
    .line 28
    new-instance p0, Lcu1;

    .line 29
    .line 30
    iget-object p1, v1, Ll11;->b:Ljava/lang/Object;

    .line 31
    .line 32
    check-cast p1, Landroid/content/Context;

    .line 33
    .line 34
    iget-object v0, v1, Ll11;->c:Ljava/lang/Object;

    .line 35
    .line 36
    check-cast v0, Ljava/lang/String;

    .line 37
    .line 38
    iget-object v2, v1, Ll11;->d:Ljava/lang/Object;

    .line 39
    .line 40
    check-cast v2, Lbm4;

    .line 41
    .line 42
    iget-boolean v1, v1, Ll11;->a:Z

    .line 43
    .line 44
    invoke-direct {p0, p1, v0, v2, v1}, Lcu1;-><init>(Landroid/content/Context;Ljava/lang/String;Lbm4;Z)V

    .line 45
    .line 46
    .line 47
    return-object p0

    .line 48
    :cond_0
    const-string p0, "Must set a non-null database name to a configuration that uses the no backup directory."

    .line 49
    .line 50
    invoke-static {p0}, Lh;->t(Ljava/lang/String;)V

    .line 51
    .line 52
    .line 53
    const/4 p0, 0x0

    .line 54
    return-object p0
.end method

.method public c(Ltr1;Ljp0;)Ljava/lang/Object;
    .locals 5

    .line 1
    iget-object v0, p0, Lfk;->f:Landroid/content/Context;

    .line 2
    .line 3
    instance-of v1, p2, Lek;

    .line 4
    .line 5
    if-eqz v1, :cond_0

    .line 6
    .line 7
    move-object v1, p2

    .line 8
    check-cast v1, Lek;

    .line 9
    .line 10
    iget v2, v1, Lek;->i:I

    .line 11
    .line 12
    const/high16 v3, -0x80000000

    .line 13
    .line 14
    and-int v4, v2, v3

    .line 15
    .line 16
    if-eqz v4, :cond_0

    .line 17
    .line 18
    sub-int/2addr v2, v3

    .line 19
    iput v2, v1, Lek;->i:I

    .line 20
    .line 21
    goto :goto_0

    .line 22
    :cond_0
    new-instance v1, Lek;

    .line 23
    .line 24
    invoke-direct {v1, p0, p2}, Lek;-><init>(Lfk;Ljp0;)V

    .line 25
    .line 26
    .line 27
    :goto_0
    iget-object p0, v1, Lek;->g:Ljava/lang/Object;

    .line 28
    .line 29
    iget p2, v1, Lek;->i:I

    .line 30
    .line 31
    const/4 v2, 0x0

    .line 32
    const/4 v3, 0x2

    .line 33
    const/4 v4, 0x1

    .line 34
    if-eqz p2, :cond_3

    .line 35
    .line 36
    if-eq p2, v4, :cond_2

    .line 37
    .line 38
    if-ne p2, v3, :cond_1

    .line 39
    .line 40
    iget-object p1, v1, Lek;->f:Ldv3;

    .line 41
    .line 42
    invoke-static {p0}, Lr33;->z(Ljava/lang/Object;)V

    .line 43
    .line 44
    .line 45
    goto :goto_3

    .line 46
    :cond_1
    const-string p0, "call to \'resume\' before \'invoke\' with coroutine"

    .line 47
    .line 48
    invoke-static {p0}, Lh;->w(Ljava/lang/String;)V

    .line 49
    .line 50
    .line 51
    return-object v2

    .line 52
    :cond_2
    invoke-static {p0}, Lr33;->z(Ljava/lang/Object;)V

    .line 53
    .line 54
    .line 55
    return-object p0

    .line 56
    :cond_3
    invoke-static {p0}, Lr33;->z(Ljava/lang/Object;)V

    .line 57
    .line 58
    .line 59
    instance-of p0, p1, Ldk;

    .line 60
    .line 61
    sget-object p2, Lwq0;->f:Lwq0;

    .line 62
    .line 63
    if-eqz p0, :cond_5

    .line 64
    .line 65
    check-cast p1, Ldk;

    .line 66
    .line 67
    invoke-virtual {p1}, Ldk;->getTypefaceLoader()Lck;

    .line 68
    .line 69
    .line 70
    move-result-object p0

    .line 71
    iput v4, v1, Lek;->i:I

    .line 72
    .line 73
    invoke-interface {p0, v0, p1, v1}, Lck;->awaitLoad(Landroid/content/Context;Ldk;Lip0;)Ljava/lang/Object;

    .line 74
    .line 75
    .line 76
    move-result-object p0

    .line 77
    if-ne p0, p2, :cond_4

    .line 78
    .line 79
    goto :goto_2

    .line 80
    :cond_4
    return-object p0

    .line 81
    :cond_5
    instance-of p0, p1, Ldv3;

    .line 82
    .line 83
    if-eqz p0, :cond_8

    .line 84
    .line 85
    move-object p0, p1

    .line 86
    check-cast p0, Ldv3;

    .line 87
    .line 88
    iput-object p0, v1, Lek;->f:Ldv3;

    .line 89
    .line 90
    iput v3, v1, Lek;->i:I

    .line 91
    .line 92
    new-instance v2, Lz70;

    .line 93
    .line 94
    invoke-static {v1}, Lx40;->C(Lip0;)Lip0;

    .line 95
    .line 96
    .line 97
    move-result-object v1

    .line 98
    invoke-direct {v2, v4, v1}, Lz70;-><init>(ILip0;)V

    .line 99
    .line 100
    .line 101
    invoke-virtual {v2}, Lz70;->u()V

    .line 102
    .line 103
    .line 104
    iget v1, p0, Ldv3;->a:I

    .line 105
    .line 106
    new-instance v4, Lv72;

    .line 107
    .line 108
    invoke-direct {v4, v3, v2, p0}, Lv72;-><init>(ILjava/lang/Object;Ljava/lang/Object;)V

    .line 109
    .line 110
    .line 111
    sget-object p0, Lhv3;->a:Ljava/lang/Object;

    .line 112
    .line 113
    invoke-virtual {v0}, Landroid/content/Context;->isRestricted()Z

    .line 114
    .line 115
    .line 116
    move-result p0

    .line 117
    if-eqz p0, :cond_6

    .line 118
    .line 119
    const/4 p0, -0x4

    .line 120
    invoke-virtual {v4, p0}, Lv72;->l(I)V

    .line 121
    .line 122
    .line 123
    goto :goto_1

    .line 124
    :cond_6
    new-instance p0, Landroid/util/TypedValue;

    .line 125
    .line 126
    invoke-direct {p0}, Landroid/util/TypedValue;-><init>()V

    .line 127
    .line 128
    .line 129
    invoke-static {v0, v1, p0, v4}, Lhv3;->b(Landroid/content/Context;ILandroid/util/TypedValue;Lv72;)Landroid/graphics/Typeface;

    .line 130
    .line 131
    .line 132
    :goto_1
    invoke-virtual {v2}, Lz70;->s()Ljava/lang/Object;

    .line 133
    .line 134
    .line 135
    move-result-object p0

    .line 136
    if-ne p0, p2, :cond_7

    .line 137
    .line 138
    :goto_2
    return-object p2

    .line 139
    :cond_7
    :goto_3
    check-cast p0, Landroid/graphics/Typeface;

    .line 140
    .line 141
    check-cast p1, Ldv3;

    .line 142
    .line 143
    iget-object p1, p1, Ldv3;->d:Lxs1;

    .line 144
    .line 145
    invoke-static {p0, p1, v0}, Lr33;->u(Landroid/graphics/Typeface;Lxs1;Landroid/content/Context;)Landroid/graphics/Typeface;

    .line 146
    .line 147
    .line 148
    move-result-object p0

    .line 149
    return-object p0

    .line 150
    :cond_8
    const-string p0, "Unknown font type: "

    .line 151
    .line 152
    invoke-static {p0, p1}, Las2;->h(Ljava/lang/String;Ljava/lang/Object;)V

    .line 153
    .line 154
    .line 155
    return-object v2
.end method

.method public d()Liu0;
    .locals 14

    .line 1
    iget-object p0, p0, Lfk;->f:Landroid/content/Context;

    .line 2
    .line 3
    if-eqz p0, :cond_0

    .line 4
    .line 5
    new-instance v0, Liu0;

    .line 6
    .line 7
    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    .line 8
    .line 9
    .line 10
    sget-object v1, Llb2;->S:Lcf1;

    .line 11
    .line 12
    invoke-static {v1}, Ls31;->a(Lwk1;)Lvp3;

    .line 13
    .line 14
    .line 15
    move-result-object v1

    .line 16
    iput-object v1, v0, Liu0;->f:Lvp3;

    .line 17
    .line 18
    new-instance v1, Ldr0;

    .line 19
    .line 20
    const/4 v2, 0x1

    .line 21
    invoke-direct {v1, p0, v2}, Ldr0;-><init>(Ljava/lang/Object;I)V

    .line 22
    .line 23
    .line 24
    iput-object v1, v0, Liu0;->g:Ldr0;

    .line 25
    .line 26
    new-instance p0, Ldr0;

    .line 27
    .line 28
    const/4 v3, 0x0

    .line 29
    invoke-direct {p0, v1, v3}, Ldr0;-><init>(Ljava/lang/Object;I)V

    .line 30
    .line 31
    .line 32
    new-instance v4, Lhx2;

    .line 33
    .line 34
    invoke-direct {v4, v1, p0, v3}, Lhx2;-><init>(Lvp3;Lvp3;I)V

    .line 35
    .line 36
    .line 37
    invoke-static {v4}, Ls31;->a(Lwk1;)Lvp3;

    .line 38
    .line 39
    .line 40
    move-result-object p0

    .line 41
    iput-object p0, v0, Liu0;->h:Lvp3;

    .line 42
    .line 43
    iget-object p0, v0, Liu0;->g:Ldr0;

    .line 44
    .line 45
    new-instance v1, Lve1;

    .line 46
    .line 47
    invoke-direct {v1, p0, v2}, Lve1;-><init>(Lvp3;I)V

    .line 48
    .line 49
    .line 50
    iput-object v1, v0, Liu0;->i:Lve1;

    .line 51
    .line 52
    new-instance v1, Lve1;

    .line 53
    .line 54
    invoke-direct {v1, p0, v3}, Lve1;-><init>(Lvp3;I)V

    .line 55
    .line 56
    .line 57
    invoke-static {v1}, Ls31;->a(Lwk1;)Lvp3;

    .line 58
    .line 59
    .line 60
    move-result-object p0

    .line 61
    iget-object v1, v0, Liu0;->i:Lve1;

    .line 62
    .line 63
    new-instance v4, Lhx2;

    .line 64
    .line 65
    invoke-direct {v4, v1, p0, v2}, Lhx2;-><init>(Lvp3;Lvp3;I)V

    .line 66
    .line 67
    .line 68
    invoke-static {v4}, Ls31;->a(Lwk1;)Lvp3;

    .line 69
    .line 70
    .line 71
    move-result-object v8

    .line 72
    iput-object v8, v0, Liu0;->j:Lvp3;

    .line 73
    .line 74
    new-instance p0, Lcf1;

    .line 75
    .line 76
    invoke-direct {p0, v2}, Lcf1;-><init>(I)V

    .line 77
    .line 78
    .line 79
    iget-object v1, v0, Liu0;->g:Ldr0;

    .line 80
    .line 81
    new-instance v9, Ll14;

    .line 82
    .line 83
    invoke-direct {v9, v1, v8, p0, v3}, Ll14;-><init>(Lvp3;Lvp3;Lwk1;I)V

    .line 84
    .line 85
    .line 86
    iget-object v6, v0, Liu0;->f:Lvp3;

    .line 87
    .line 88
    iget-object v7, v0, Liu0;->h:Lvp3;

    .line 89
    .line 90
    new-instance v5, Lnx0;

    .line 91
    .line 92
    move-object v10, v8

    .line 93
    move-object v13, v9

    .line 94
    move-object v9, v8

    .line 95
    move-object v8, v13

    .line 96
    invoke-direct/range {v5 .. v10}, Lnx0;-><init>(Lvp3;Lvp3;Ll14;Lvp3;Lvp3;)V

    .line 97
    .line 98
    .line 99
    move-object p0, v9

    .line 100
    move-object v9, v8

    .line 101
    move-object v8, p0

    .line 102
    move-object p0, v5

    .line 103
    new-instance v5, Le65;

    .line 104
    .line 105
    move-object v11, v8

    .line 106
    move-object v12, v8

    .line 107
    move-object v10, v6

    .line 108
    move-object v6, v1

    .line 109
    invoke-direct/range {v5 .. v12}, Le65;-><init>(Lvp3;Lvp3;Lvp3;Ll14;Lvp3;Lvp3;Lvp3;)V

    .line 110
    .line 111
    .line 112
    move-object v6, v10

    .line 113
    new-instance v1, Lge5;

    .line 114
    .line 115
    invoke-direct {v1, v6, v8, v9, v8}, Lge5;-><init>(Lvp3;Lvp3;Ll14;Lvp3;)V

    .line 116
    .line 117
    .line 118
    new-instance v3, Ll14;

    .line 119
    .line 120
    invoke-direct {v3, p0, v5, v1, v2}, Ll14;-><init>(Lvp3;Lvp3;Lwk1;I)V

    .line 121
    .line 122
    .line 123
    invoke-static {v3}, Ls31;->a(Lwk1;)Lvp3;

    .line 124
    .line 125
    .line 126
    move-result-object p0

    .line 127
    iput-object p0, v0, Liu0;->k:Lvp3;

    .line 128
    .line 129
    return-object v0

    .line 130
    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    .line 131
    .line 132
    const-class v0, Landroid/content/Context;

    .line 133
    .line 134
    invoke-virtual {v0}, Ljava/lang/Class;->getCanonicalName()Ljava/lang/String;

    .line 135
    .line 136
    .line 137
    move-result-object v0

    .line 138
    new-instance v1, Ljava/lang/StringBuilder;

    .line 139
    .line 140
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    .line 141
    .line 142
    .line 143
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 144
    .line 145
    .line 146
    const-string v0, " must be set"

    .line 147
    .line 148
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 149
    .line 150
    .line 151
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    .line 152
    .line 153
    .line 154
    move-result-object v0

    .line 155
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    .line 156
    .line 157
    .line 158
    throw p0
.end method

.method public f(Ltr1;)Landroid/graphics/Typeface;
    .locals 1

    .line 1
    iget-object p0, p0, Lfk;->f:Landroid/content/Context;

    .line 2
    .line 3
    instance-of v0, p1, Ldk;

    .line 4
    .line 5
    if-eqz v0, :cond_0

    .line 6
    .line 7
    check-cast p1, Ldk;

    .line 8
    .line 9
    invoke-virtual {p1}, Ldk;->getTypefaceLoader()Lck;

    .line 10
    .line 11
    .line 12
    move-result-object v0

    .line 13
    invoke-interface {v0, p0, p1}, Lck;->loadBlocking(Landroid/content/Context;Ldk;)Landroid/graphics/Typeface;

    .line 14
    .line 15
    .line 16
    move-result-object p0

    .line 17
    return-object p0

    .line 18
    :cond_0
    instance-of v0, p1, Ldv3;

    .line 19
    .line 20
    if-eqz v0, :cond_1

    .line 21
    .line 22
    check-cast p1, Ldv3;

    .line 23
    .line 24
    iget v0, p1, Ldv3;->a:I

    .line 25
    .line 26
    invoke-static {p0, v0}, Lhv3;->a(Landroid/content/Context;I)Landroid/graphics/Typeface;

    .line 27
    .line 28
    .line 29
    move-result-object v0

    .line 30
    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 31
    .line 32
    .line 33
    iget-object p1, p1, Ldv3;->d:Lxs1;

    .line 34
    .line 35
    invoke-static {v0, p1, p0}, Lr33;->u(Landroid/graphics/Typeface;Lxs1;Landroid/content/Context;)Landroid/graphics/Typeface;

    .line 36
    .line 37
    .line 38
    move-result-object p0

    .line 39
    return-object p0

    .line 40
    :cond_1
    const/4 p0, 0x0

    .line 41
    return-object p0
.end method

.method public g(Leg;Ljava/time/Instant;IIZZ)Landroid/graphics/Bitmap;
    .locals 33

    .line 1
    move-object/from16 v1, p1

    .line 2
    .line 3
    move/from16 v0, p3

    .line 4
    .line 5
    move/from16 v2, p4

    .line 6
    .line 7
    move/from16 v4, p5

    .line 8
    .line 9
    invoke-virtual {v1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 10
    .line 11
    .line 12
    const/4 v3, 0x0

    .line 13
    invoke-static {v0, v2, v3}, Lp60;->i(III)Lkk;

    .line 14
    .line 15
    .line 16
    move-result-object v9

    .line 17
    move-object/from16 v3, p0

    .line 18
    .line 19
    iget-object v3, v3, Lfk;->f:Landroid/content/Context;

    .line 20
    .line 21
    invoke-virtual {v3}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    .line 22
    .line 23
    .line 24
    move-result-object v5

    .line 25
    invoke-virtual {v5}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    .line 26
    .line 27
    .line 28
    move-result-object v5

    .line 29
    iget v5, v5, Landroid/util/DisplayMetrics;->density:F

    .line 30
    .line 31
    invoke-virtual {v3}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    .line 32
    .line 33
    .line 34
    move-result-object v6

    .line 35
    invoke-virtual {v6}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    .line 36
    .line 37
    .line 38
    move-result-object v6

    .line 39
    iget v6, v6, Landroid/content/res/Configuration;->fontScale:F

    .line 40
    .line 41
    new-instance v7, Lnz0;

    .line 42
    .line 43
    invoke-direct {v7, v5, v6}, Lnz0;-><init>(FF)V

    .line 44
    .line 45
    .line 46
    invoke-static {v3}, Landroid/text/format/DateFormat;->is24HourFormat(Landroid/content/Context;)Z

    .line 47
    .line 48
    .line 49
    move-result v16

    .line 50
    new-instance v15, Landroid/graphics/Paint;

    .line 51
    .line 52
    const/4 v3, 0x1

    .line 53
    invoke-direct {v15, v3}, Landroid/graphics/Paint;-><init>(I)V

    .line 54
    .line 55
    .line 56
    const/high16 v6, -0x1000000

    .line 57
    .line 58
    const/4 v8, -0x1

    .line 59
    if-eqz v4, :cond_0

    .line 60
    .line 61
    move v10, v8

    .line 62
    goto :goto_0

    .line 63
    :cond_0
    move v10, v6

    .line 64
    :goto_0
    invoke-virtual {v15, v10}, Landroid/graphics/Paint;->setColor(I)V

    .line 65
    .line 66
    .line 67
    sget-object v10, Landroid/graphics/Paint$Align;->CENTER:Landroid/graphics/Paint$Align;

    .line 68
    .line 69
    invoke-virtual {v15, v10}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V

    .line 70
    .line 71
    .line 72
    const/high16 v11, 0x41500000    # 13.0f

    .line 73
    .line 74
    mul-float/2addr v11, v5

    .line 75
    invoke-virtual {v15, v11}, Landroid/graphics/Paint;->setTextSize(F)V

    .line 76
    .line 77
    .line 78
    new-instance v11, Landroid/graphics/Paint;

    .line 79
    .line 80
    invoke-direct {v11, v3}, Landroid/graphics/Paint;-><init>(I)V

    .line 81
    .line 82
    .line 83
    if-eqz v4, :cond_1

    .line 84
    .line 85
    move v6, v8

    .line 86
    :cond_1
    invoke-virtual {v11, v6}, Landroid/graphics/Paint;->setColor(I)V

    .line 87
    .line 88
    .line 89
    invoke-virtual {v11, v10}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V

    .line 90
    .line 91
    .line 92
    const/high16 v3, 0x41600000    # 14.0f

    .line 93
    .line 94
    mul-float/2addr v3, v5

    .line 95
    invoke-virtual {v11, v3}, Landroid/graphics/Paint;->setTextSize(F)V

    .line 96
    .line 97
    .line 98
    new-instance v10, Lg80;

    .line 99
    .line 100
    invoke-direct {v10}, Lg80;-><init>()V

    .line 101
    .line 102
    .line 103
    invoke-static {v9}, Lu40;->b(Lkk;)Ljh;

    .line 104
    .line 105
    .line 106
    move-result-object v3

    .line 107
    int-to-float v0, v0

    .line 108
    int-to-float v2, v2

    .line 109
    invoke-static {v0}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 110
    .line 111
    .line 112
    move-result v0

    .line 113
    int-to-long v12, v0

    .line 114
    invoke-static {v2}, Ljava/lang/Float;->floatToRawIntBits(F)I

    .line 115
    .line 116
    .line 117
    move-result v0

    .line 118
    move v2, v5

    .line 119
    int-to-long v5, v0

    .line 120
    const/16 v24, 0x20

    .line 121
    .line 122
    shl-long v12, v12, v24

    .line 123
    .line 124
    const-wide v25, 0xffffffffL

    .line 125
    .line 126
    .line 127
    .line 128
    .line 129
    and-long v5, v5, v25

    .line 130
    .line 131
    or-long/2addr v5, v12

    .line 132
    iget-object v0, v10, Lg80;->f:Lf80;

    .line 133
    .line 134
    iget-object v8, v0, Lf80;->a:Lkz0;

    .line 135
    .line 136
    iget-object v12, v0, Lf80;->b:Lqh2;

    .line 137
    .line 138
    iget-object v13, v0, Lf80;->c:Le80;

    .line 139
    .line 140
    move-object/from16 p0, v8

    .line 141
    .line 142
    move-object/from16 v27, v9

    .line 143
    .line 144
    iget-wide v8, v0, Lf80;->d:J

    .line 145
    .line 146
    iput-object v7, v0, Lf80;->a:Lkz0;

    .line 147
    .line 148
    sget-object v14, Lqh2;->f:Lqh2;

    .line 149
    .line 150
    iput-object v14, v0, Lf80;->b:Lqh2;

    .line 151
    .line 152
    iput-object v3, v0, Lf80;->c:Le80;

    .line 153
    .line 154
    iput-wide v5, v0, Lf80;->d:J

    .line 155
    .line 156
    invoke-virtual {v3}, Ljh;->m()V

    .line 157
    .line 158
    .line 159
    invoke-virtual {v15}, Landroid/graphics/Paint;->getTextSize()F

    .line 160
    .line 161
    .line 162
    move-result v14

    .line 163
    const/high16 v5, 0x40e00000    # 7.0f

    .line 164
    .line 165
    mul-float/2addr v2, v5

    .line 166
    iget-object v5, v10, Lg80;->g:Ler;

    .line 167
    .line 168
    iget-object v6, v5, Ler;->g:Ljava/lang/Object;

    .line 169
    .line 170
    check-cast v6, Lnx3;

    .line 171
    .line 172
    move-object/from16 p3, v0

    .line 173
    .line 174
    const/4 v0, 0x0

    .line 175
    invoke-virtual {v6, v2, v0, v0, v0}, Lnx3;->p(FFFF)V

    .line 176
    .line 177
    .line 178
    :try_start_0
    invoke-interface {v10}, Lb61;->c()J

    .line 179
    .line 180
    .line 181
    move-result-wide v17

    .line 182
    move-object/from16 v19, v7

    .line 183
    .line 184
    shr-long v6, v17, v24

    .line 185
    .line 186
    long-to-int v6, v6

    .line 187
    invoke-static {v6}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 188
    .line 189
    .line 190
    move-result v6

    .line 191
    iget v7, v1, Leg;->d:F

    .line 192
    .line 193
    div-float v20, v6, v7

    .line 194
    .line 195
    move-object/from16 v23, v11

    .line 196
    .line 197
    iget-object v11, v1, Leg;->f:Lkw;

    .line 198
    .line 199
    invoke-interface {v10}, Lb61;->c()J

    .line 200
    .line 201
    .line 202
    move-result-wide v6

    .line 203
    shr-long v6, v6, v24

    .line 204
    .line 205
    long-to-int v6, v6

    .line 206
    invoke-static {v6}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 207
    .line 208
    .line 209
    move-result v6

    .line 210
    move-object v7, v13

    .line 211
    move v13, v6

    .line 212
    move-object v6, v12

    .line 213
    move/from16 v12, v20

    .line 214
    .line 215
    invoke-static/range {v10 .. v16}, Lzv0;->E(Lb61;Lkw;FFFLandroid/graphics/Paint;Z)V

    .line 216
    .line 217
    .line 218
    move/from16 v30, v14

    .line 219
    .line 220
    move-object/from16 v29, v15

    .line 221
    .line 222
    move/from16 v28, v16

    .line 223
    .line 224
    const/high16 v11, 0x3fc00000    # 1.5f

    .line 225
    .line 226
    mul-float v11, v11, v30

    .line 227
    .line 228
    iget-object v13, v5, Ler;->g:Ljava/lang/Object;

    .line 229
    .line 230
    check-cast v13, Lnx3;

    .line 231
    .line 232
    invoke-virtual {v13, v0, v11, v0, v11}, Lnx3;->p(FFFF)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_5

    .line 233
    .line 234
    .line 235
    :try_start_1
    invoke-interface {v10}, Lb61;->c()J

    .line 236
    .line 237
    .line 238
    move-result-wide v13

    .line 239
    and-long v13, v13, v25

    .line 240
    .line 241
    long-to-int v0, v13

    .line 242
    invoke-static {v0}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 243
    .line 244
    .line 245
    move-result v21

    .line 246
    iget-object v0, v1, Leg;->e:Ljava/util/List;

    .line 247
    .line 248
    invoke-interface {v0}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    .line 249
    .line 250
    .line 251
    move-result-object v0

    .line 252
    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    .line 253
    .line 254
    .line 255
    move-result v13
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_4

    .line 256
    if-eqz v13, :cond_2

    .line 257
    .line 258
    :try_start_2
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    .line 259
    .line 260
    .line 261
    move-result-object v13

    .line 262
    check-cast v13, Lmz1;

    .line 263
    .line 264
    iget-object v14, v13, Lmz1;->b:Lw8;

    .line 265
    .line 266
    invoke-virtual {v14, v4}, Lw8;->a(Z)J

    .line 267
    .line 268
    .line 269
    move-result-wide v14
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    .line 270
    move-wide/from16 v31, v8

    .line 271
    .line 272
    move v9, v11

    .line 273
    move-object/from16 v16, v19

    .line 274
    .line 275
    move-object v11, v10

    .line 276
    move-object v10, v13

    .line 277
    move v13, v12

    .line 278
    move/from16 v12, v21

    .line 279
    .line 280
    :try_start_3
    invoke-virtual/range {v10 .. v16}, Lmz1;->e(Lb61;FFJLkz0;)V

    .line 281
    .line 282
    .line 283
    move-object v10, v11

    .line 284
    move/from16 v21, v12

    .line 285
    .line 286
    move v12, v13

    .line 287
    move v11, v9

    .line 288
    move-object/from16 v19, v16

    .line 289
    .line 290
    move-wide/from16 v8, v31

    .line 291
    .line 292
    goto :goto_1

    .line 293
    :catchall_0
    move-exception v0

    .line 294
    :goto_2
    move v11, v2

    .line 295
    move-object v15, v5

    .line 296
    const/high16 v14, -0x80000000

    .line 297
    .line 298
    goto/16 :goto_6

    .line 299
    .line 300
    :catchall_1
    move-exception v0

    .line 301
    move v9, v11

    .line 302
    goto :goto_2

    .line 303
    :cond_2
    move-wide/from16 v31, v8

    .line 304
    .line 305
    move v9, v11

    .line 306
    move-object/from16 v16, v19

    .line 307
    .line 308
    iget-object v0, v1, Leg;->a:Ljava/util/List;

    .line 309
    .line 310
    invoke-interface {v0}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    .line 311
    .line 312
    .line 313
    move-result-object v0

    .line 314
    :goto_3
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    .line 315
    .line 316
    .line 317
    move-result v8

    .line 318
    if-eqz v8, :cond_3

    .line 319
    .line 320
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    .line 321
    .line 322
    .line 323
    move-result-object v8

    .line 324
    check-cast v8, Llu0;

    .line 325
    .line 326
    iget-object v11, v1, Leg;->c:Ljava/time/Instant;

    .line 327
    .line 328
    iget-object v13, v8, Llu0;->a:Ljava/time/Instant;

    .line 329
    .line 330
    iget-object v8, v8, Llu0;->b:Lt94;

    .line 331
    .line 332
    move-object/from16 v22, v8

    .line 333
    .line 334
    move-object/from16 v17, v10

    .line 335
    .line 336
    move-object/from16 v18, v11

    .line 337
    .line 338
    move/from16 v20, v12

    .line 339
    .line 340
    move-object/from16 v19, v13

    .line 341
    .line 342
    invoke-static/range {v17 .. v23}, Lzv0;->H(Lb61;Ljava/time/Instant;Ljava/time/Instant;FFLt94;Landroid/graphics/Paint;)V

    .line 343
    .line 344
    .line 345
    move-object/from16 v10, v17

    .line 346
    .line 347
    move/from16 v12, v20

    .line 348
    .line 349
    goto :goto_3

    .line 350
    :cond_3
    iget-object v0, v1, Leg;->b:Ljava/util/List;

    .line 351
    .line 352
    invoke-interface {v0}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    .line 353
    .line 354
    .line 355
    move-result-object v0

    .line 356
    :goto_4
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    .line 357
    .line 358
    .line 359
    move-result v8

    .line 360
    if-eqz v8, :cond_4

    .line 361
    .line 362
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    .line 363
    .line 364
    .line 365
    move-result-object v8

    .line 366
    check-cast v8, Lmu0;

    .line 367
    .line 368
    move-object v11, v3

    .line 369
    iget-object v3, v1, Leg;->c:Ljava/time/Instant;

    .line 370
    .line 371
    iget-object v4, v8, Lmu0;->a:Ljava/time/Instant;

    .line 372
    .line 373
    iget-object v8, v8, Lmu0;->b:Lw8;
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    .line 374
    .line 375
    move-object v15, v5

    .line 376
    move-object v13, v7

    .line 377
    move-object v7, v8

    .line 378
    move-object/from16 v17, v11

    .line 379
    .line 380
    move v5, v12

    .line 381
    const/high16 v14, -0x80000000

    .line 382
    .line 383
    move/from16 v8, p5

    .line 384
    .line 385
    move v11, v2

    .line 386
    move-object v12, v6

    .line 387
    move-object v2, v10

    .line 388
    move/from16 v6, v21

    .line 389
    .line 390
    move-object/from16 v10, p0

    .line 391
    .line 392
    :try_start_4
    invoke-static/range {v2 .. v8}, Lzv0;->I(Lb61;Ljava/time/Instant;Ljava/time/Instant;FFLw8;Z)V

    .line 393
    .line 394
    .line 395
    move v3, v5

    .line 396
    move/from16 v21, v6

    .line 397
    .line 398
    move/from16 v4, p5

    .line 399
    .line 400
    move-object/from16 p0, v10

    .line 401
    .line 402
    move-object v6, v12

    .line 403
    move-object v7, v13

    .line 404
    move-object v5, v15

    .line 405
    move-object v10, v2

    .line 406
    move v12, v3

    .line 407
    move v2, v11

    .line 408
    move-object/from16 v3, v17

    .line 409
    .line 410
    goto :goto_4

    .line 411
    :catchall_2
    move-exception v0

    .line 412
    goto/16 :goto_6

    .line 413
    .line 414
    :cond_4
    move v11, v2

    .line 415
    move-object/from16 v17, v3

    .line 416
    .line 417
    move-object v15, v5

    .line 418
    move-object v13, v7

    .line 419
    move-object v2, v10

    .line 420
    move v3, v12

    .line 421
    const/high16 v14, -0x80000000

    .line 422
    .line 423
    move-object/from16 v10, p0

    .line 424
    .line 425
    move-object v12, v6

    .line 426
    if-eqz p6, :cond_5

    .line 427
    .line 428
    move-object/from16 v6, p3

    .line 429
    .line 430
    move/from16 v4, p5

    .line 431
    .line 432
    move-object v0, v2

    .line 433
    move-object/from16 v5, v16

    .line 434
    .line 435
    move-object/from16 v2, p2

    .line 436
    .line 437
    invoke-static/range {v0 .. v5}, Lfk;->e(Lg80;Leg;Ljava/time/Instant;FZLnz0;)V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_2

    .line 438
    .line 439
    .line 440
    move-object v2, v0

    .line 441
    goto :goto_5

    .line 442
    :cond_5
    move-object/from16 v6, p3

    .line 443
    .line 444
    :goto_5
    :try_start_5
    iget-object v0, v15, Ler;->g:Ljava/lang/Object;

    .line 445
    .line 446
    check-cast v0, Lnx3;

    .line 447
    .line 448
    neg-float v4, v9

    .line 449
    invoke-virtual {v0, v14, v4, v14, v4}, Lnx3;->p(FFFF)V

    .line 450
    .line 451
    .line 452
    iget-object v0, v1, Leg;->f:Lkw;

    .line 453
    .line 454
    invoke-interface {v2}, Lb61;->c()J

    .line 455
    .line 456
    .line 457
    move-result-wide v4

    .line 458
    shr-long v4, v4, v24

    .line 459
    .line 460
    long-to-int v1, v4

    .line 461
    invoke-static {v1}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 462
    .line 463
    .line 464
    move-result v1

    .line 465
    invoke-interface {v2}, Lb61;->c()J

    .line 466
    .line 467
    .line 468
    move-result-wide v4

    .line 469
    and-long v4, v4, v25

    .line 470
    .line 471
    long-to-int v4, v4

    .line 472
    invoke-static {v4}, Ljava/lang/Float;->intBitsToFloat(I)F

    .line 473
    .line 474
    .line 475
    move-result v4

    .line 476
    const/high16 v5, 0x3e800000    # 0.25f

    .line 477
    .line 478
    mul-float v5, v5, v30

    .line 479
    .line 480
    sub-float/2addr v4, v5

    .line 481
    move-object/from16 p1, v0

    .line 482
    .line 483
    move/from16 p3, v1

    .line 484
    .line 485
    move-object/from16 p0, v2

    .line 486
    .line 487
    move/from16 p2, v3

    .line 488
    .line 489
    move/from16 p4, v4

    .line 490
    .line 491
    move/from16 p6, v28

    .line 492
    .line 493
    move-object/from16 p5, v29

    .line 494
    .line 495
    invoke-static/range {p0 .. p6}, Lzv0;->E(Lb61;Lkw;FFFLandroid/graphics/Paint;Z)V
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_3

    .line 496
    .line 497
    .line 498
    iget-object v0, v15, Ler;->g:Ljava/lang/Object;

    .line 499
    .line 500
    check-cast v0, Lnx3;

    .line 501
    .line 502
    neg-float v1, v11

    .line 503
    invoke-virtual {v0, v1, v14, v14, v14}, Lnx3;->p(FFFF)V

    .line 504
    .line 505
    .line 506
    invoke-virtual/range {v17 .. v17}, Ljh;->k()V

    .line 507
    .line 508
    .line 509
    iput-object v10, v6, Lf80;->a:Lkz0;

    .line 510
    .line 511
    iput-object v12, v6, Lf80;->b:Lqh2;

    .line 512
    .line 513
    iput-object v13, v6, Lf80;->c:Le80;

    .line 514
    .line 515
    move-wide/from16 v0, v31

    .line 516
    .line 517
    iput-wide v0, v6, Lf80;->d:J

    .line 518
    .line 519
    invoke-static/range {v27 .. v27}, Lzv0;->w(Lkk;)Landroid/graphics/Bitmap;

    .line 520
    .line 521
    .line 522
    move-result-object v0

    .line 523
    return-object v0

    .line 524
    :catchall_3
    move-exception v0

    .line 525
    goto :goto_7

    .line 526
    :catchall_4
    move-exception v0

    .line 527
    move-object v15, v5

    .line 528
    move v9, v11

    .line 529
    const/high16 v14, -0x80000000

    .line 530
    .line 531
    move v11, v2

    .line 532
    :goto_6
    :try_start_6
    iget-object v1, v15, Ler;->g:Ljava/lang/Object;

    .line 533
    .line 534
    check-cast v1, Lnx3;

    .line 535
    .line 536
    neg-float v2, v9

    .line 537
    invoke-virtual {v1, v14, v2, v14, v2}, Lnx3;->p(FFFF)V

    .line 538
    .line 539
    .line 540
    throw v0
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_3

    .line 541
    :catchall_5
    move-exception v0

    .line 542
    move v11, v2

    .line 543
    move-object v15, v5

    .line 544
    const/high16 v14, -0x80000000

    .line 545
    .line 546
    :goto_7
    iget-object v1, v15, Ler;->g:Ljava/lang/Object;

    .line 547
    .line 548
    check-cast v1, Lnx3;

    .line 549
    .line 550
    neg-float v2, v11

    .line 551
    invoke-virtual {v1, v2, v14, v14, v14}, Lnx3;->p(FFFF)V

    .line 552
    .line 553
    .line 554
    throw v0
.end method
