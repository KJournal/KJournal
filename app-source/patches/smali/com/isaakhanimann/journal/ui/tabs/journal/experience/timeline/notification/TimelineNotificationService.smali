.class public final Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;
.super Landroid/app/Service;
.source "r8-map-id-290ebb60cd1ac122145cca66461ed9e7d2f764a7712c78a8a3c838fecaf4f98f"

# interfaces
.implements Lew1;


# static fields
.field public static final p:Log4;

.field public static final q:Lar3;


# instance fields
.field public volatile f:Lu64;

.field public final g:Ljava/lang/Object;

.field public h:Z

.field public i:Lw64;

.field public j:Lfk;

.field public k:Lrh1;

.field public l:Lc75;

.field public final m:Lep0;

.field public n:Lqf4;

.field public o:Z


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .line 1
    const/4 v0, 0x0

    .line 2
    invoke-static {v0}, Lh42;->N(Ljava/lang/Object;)Log4;

    .line 3
    .line 4
    .line 5
    move-result-object v0

    .line 6
    sput-object v0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->p:Log4;

    .line 7
    .line 8
    invoke-static {v0}, La70;->t(Lk13;)Lar3;

    .line 9
    .line 10
    .line 11
    move-result-object v0

    .line 12
    sput-object v0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->q:Lar3;

    .line 13
    .line 14
    return-void
.end method

.method public constructor <init>()V
    .locals 2

    .line 1
    invoke-direct {p0}, Landroid/app/Service;-><init>()V

    .line 2
    .line 3
    .line 4
    new-instance v0, Ljava/lang/Object;

    .line 5
    .line 6
    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    .line 7
    .line 8
    .line 9
    iput-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->g:Ljava/lang/Object;

    .line 10
    .line 11
    const/4 v0, 0x0

    .line 12
    iput-boolean v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->h:Z

    .line 13
    .line 14
    invoke-static {}, Lb63;->h()Lyl4;

    .line 15
    .line 16
    .line 17
    move-result-object v0

    .line 18
    sget-object v1, Lw11;->a:Llx0;

    .line 19
    .line 20
    sget-object v1, Lju2;->a:Lxz1;

    .line 21
    .line 22
    iget-object v1, v1, Lxz1;->k:Lxz1;

    .line 23
    .line 24
    invoke-static {v0, v1}, Lg70;->K(Lkq0;Lmq0;)Lmq0;

    .line 25
    .line 26
    .line 27
    move-result-object v0

    .line 28
    invoke-static {v0}, Lu40;->e(Lmq0;)Lep0;

    .line 29
    .line 30
    .line 31
    move-result-object v0

    .line 32
    iput-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->m:Lep0;

    .line 33
    .line 34
    return-void
.end method

.method public static final b(Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;ILeg;Ljp0;)Ljava/lang/Object;
    .locals 10

    .line 1
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 2
    .line 3
    .line 4
    instance-of v0, p3, Lgw4;

    .line 5
    .line 6
    if-eqz v0, :cond_0

    .line 7
    .line 8
    move-object v0, p3

    .line 9
    check-cast v0, Lgw4;

    .line 10
    .line 11
    iget v1, v0, Lgw4;->i:I

    .line 12
    .line 13
    const/high16 v2, -0x80000000

    .line 14
    .line 15
    and-int v3, v1, v2

    .line 16
    .line 17
    if-eqz v3, :cond_0

    .line 18
    .line 19
    sub-int/2addr v1, v2

    .line 20
    iput v1, v0, Lgw4;->i:I

    .line 21
    .line 22
    goto :goto_0

    .line 23
    :cond_0
    new-instance v0, Lgw4;

    .line 24
    .line 25
    invoke-direct {v0, p0, p3}, Lgw4;-><init>(Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;Ljp0;)V

    .line 26
    .line 27
    .line 28
    :goto_0
    iget-object p3, v0, Lgw4;->g:Ljava/lang/Object;

    .line 29
    .line 30
    iget v1, v0, Lgw4;->i:I

    .line 31
    .line 32
    const/4 v2, 0x0

    .line 33
    const/4 v3, 0x1

    .line 34
    if-eqz v1, :cond_2

    .line 35
    .line 36
    if-ne v1, v3, :cond_1

    .line 37
    .line 38
    iget p1, v0, Lgw4;->f:I

    .line 39
    .line 40
    invoke-static {p3}, Lr33;->z(Ljava/lang/Object;)V

    .line 41
    .line 42
    .line 43
    goto :goto_2

    .line 44
    :cond_1
    const-string p0, "call to \'resume\' before \'invoke\' with coroutine"

    .line 45
    .line 46
    invoke-static {p0}, Lh;->w(Ljava/lang/String;)V

    .line 47
    .line 48
    .line 49
    return-object v2

    .line 50
    :cond_2
    invoke-static {p3}, Lr33;->z(Ljava/lang/Object;)V

    .line 51
    .line 52
    .line 53
    invoke-static {p0}, Le75;->l(Landroid/content/Context;)Z

    .line 54
    .line 55
    .line 56
    move-result p3

    .line 57
    if-nez p3, :cond_3

    .line 58
    .line 59
    sget-object p0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    .line 60
    .line 61
    return-object p0

    .line 62
    :cond_3
    invoke-static {}, Ljava/time/Instant;->now()Ljava/time/Instant;

    .line 63
    .line 64
    .line 65
    move-result-object v7

    .line 66
    invoke-virtual {v7}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 67
    .line 68
    .line 69
    invoke-virtual {p2}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 70
    .line 71
    .line 72
    iget-object p3, p2, Leg;->c:Ljava/time/Instant;

    .line 73
    .line 74
    iget v1, p2, Leg;->d:F

    .line 75
    .line 76
    float-to-long v4, v1

    .line 77
    invoke-virtual {p3, v4, v5}, Ljava/time/Instant;->plusSeconds(J)Ljava/time/Instant;

    .line 78
    .line 79
    .line 80
    move-result-object p3

    .line 81
    invoke-virtual {p3}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 82
    .line 83
    .line 84
    invoke-virtual {p3, v7}, Ljava/time/Instant;->isAfter(Ljava/time/Instant;)Z

    .line 85
    .line 86
    .line 87
    move-result p3

    .line 88
    if-nez p3, :cond_4

    .line 89
    .line 90
    sget-object p0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    .line 91
    .line 92
    return-object p0

    .line 93
    :cond_4
    iget-object v5, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->j:Lfk;

    .line 94
    .line 95
    if-eqz v5, :cond_7

    .line 96
    .line 97
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    .line 98
    .line 99
    .line 100
    move-result-object p3

    .line 101
    invoke-virtual {p3}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    .line 102
    .line 103
    .line 104
    move-result-object p3

    .line 105
    iget p3, p3, Landroid/content/res/Configuration;->uiMode:I

    .line 106
    .line 107
    and-int/lit8 p3, p3, 0x30

    .line 108
    .line 109
    const/16 v1, 0x20

    .line 110
    .line 111
    if-ne p3, v1, :cond_5

    .line 112
    .line 113
    move v8, v3

    .line 114
    goto :goto_1

    .line 115
    :cond_5
    const/4 p3, 0x0

    .line 116
    move v8, p3

    .line 117
    :goto_1
    iput p1, v0, Lgw4;->f:I

    .line 118
    .line 119
    iput v3, v0, Lgw4;->i:I

    .line 120
    .line 121
    sget-object p3, Lw11;->a:Llx0;

    .line 122
    .line 123
    new-instance v4, Lpv4;

    .line 124
    .line 125
    const/4 v9, 0x0

    .line 126
    move-object v6, p2

    .line 127
    invoke-direct/range {v4 .. v9}, Lpv4;-><init>(Lfk;Leg;Ljava/time/Instant;ZLip0;)V

    .line 128
    .line 129
    .line 130
    invoke-static {p3, v4, v0}, Lkb3;->E(Lmq0;Lev1;Lip0;)Ljava/lang/Object;

    .line 131
    .line 132
    .line 133
    move-result-object p3

    .line 134
    sget-object p2, Lwq0;->f:Lwq0;

    .line 135
    .line 136
    if-ne p3, p2, :cond_6

    .line 137
    .line 138
    return-object p2

    .line 139
    :cond_6
    :goto_2
    check-cast p3, Landroid/graphics/Bitmap;

    .line 140
    .line 141
    new-instance p2, Landroid/widget/RemoteViews;

    .line 142
    .line 143
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    .line 144
    .line 145
    .line 146
    move-result-object v0

    .line 147
    const v1, 0x7f0c025a

    .line 148
    .line 149
    .line 150
    invoke-direct {p2, v0, v1}, Landroid/widget/RemoteViews;-><init>(Ljava/lang/String;I)V

    .line 151
    .line 152
    .line 153
    const v0, 0x7f0900ea

    .line 154
    .line 155
    .line 156
    invoke-virtual {p2, v0, p3}, Landroid/widget/RemoteViews;->setImageViewBitmap(ILandroid/graphics/Bitmap;)V

    .line 157
    .line 158
    .line 159
    new-instance p3, Ln83;

    .line 160
    .line 161
    const-string v0, "live_timeline"

    .line 162
    .line 163
    invoke-direct {p3, p0, v0}, Ln83;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    .line 164
    .line 165
    .line 166
    const v0, 0x7f08005a

    .line 167
    .line 168
    .line 169
    iget-object v1, p3, Ln83;->q:Landroid/app/Notification;

    .line 170
    .line 171
    iput v0, v1, Landroid/app/Notification;->icon:I

    .line 172
    .line 173
    const-string v0, "\ud6a8\uacfc \ud0c0\uc784\ub77c\uc778"

    .line 174
    .line 175
    invoke-static {v0}, Ln83;->b(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;

    .line 176
    .line 177
    .line 178
    move-result-object v0

    .line 179
    iput-object v0, p3, Ln83;->e:Ljava/lang/CharSequence;

    .line 180
    .line 181
    invoke-virtual {p0, p1}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f(I)Landroid/app/PendingIntent;

    .line 182
    .line 183
    .line 184
    move-result-object p1

    .line 185
    iput-object p1, p3, Ln83;->g:Landroid/app/PendingIntent;

    .line 186
    .line 187
    iput-object p2, p3, Ln83;->n:Landroid/widget/RemoteViews;

    .line 188
    .line 189
    new-instance p1, Lp83;

    .line 190
    .line 191
    invoke-direct {p1}, Ljava/lang/Object;-><init>()V

    .line 192
    .line 193
    .line 194
    invoke-virtual {p3, p1}, Ln83;->d(Lem5;)V

    .line 195
    .line 196
    .line 197
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->c()Ll83;

    .line 198
    .line 199
    .line 200
    move-result-object p1

    .line 201
    iget-object p2, p3, Ln83;->b:Ljava/util/ArrayList;

    .line 202
    .line 203
    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 204
    .line 205
    .line 206
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->g()Ll83;

    .line 207
    .line 208
    .line 209
    move-result-object p1

    .line 210
    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 211
    .line 212
    .line 213
    const/4 p1, 0x2

    .line 214
    invoke-virtual {p3, p1}, Ln83;->c(I)V

    .line 215
    .line 216
    .line 217
    const/16 p1, 0x8

    .line 218
    .line 219
    invoke-virtual {p3, p1}, Ln83;->c(I)V

    .line 220
    .line 221
    .line 222
    iput-boolean v3, p3, Ln83;->r:Z

    .line 223
    .line 224
    invoke-virtual {p3}, Ln83;->a()Landroid/app/Notification;

    .line 225
    .line 226
    .line 227
    move-result-object p1

    .line 228
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 229
    .line 230
    .line 231
    :try_start_0
    new-instance p2, Lv83;

    .line 232
    .line 233
    invoke-direct {p2, p0}, Lv83;-><init>(Landroid/content/Context;)V

    .line 234
    .line 235
    .line 236
    invoke-virtual {p2, p1}, Lv83;->a(Landroid/app/Notification;)V
    :try_end_0
    .catch Ljava/lang/SecurityException; {:try_start_0 .. :try_end_0} :catch_0

    .line 237
    .line 238
    .line 239
    sget-object p0, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    .line 240
    .line 241
    return-object p0

    .line 242
    :catch_0
    sget-object p0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    .line 243
    .line 244
    return-object p0

    .line 245
    :cond_7
    const-string p0, "bitmapRenderer"

    .line 246
    .line 247
    invoke-static {p0}, Llb2;->N(Ljava/lang/String;)V

    .line 248
    .line 249
    .line 250
    throw v2
.end method


# virtual methods
.method public final a()Ljava/lang/Object;
    .locals 2

    .line 1
    iget-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f:Lu64;

    .line 2
    .line 3
    if-nez v0, :cond_1

    .line 4
    .line 5
    iget-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->g:Ljava/lang/Object;

    .line 6
    .line 7
    monitor-enter v0

    .line 8
    :try_start_0
    iget-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f:Lu64;

    .line 9
    .line 10
    if-nez v1, :cond_0

    .line 11
    .line 12
    new-instance v1, Lu64;

    .line 13
    .line 14
    invoke-direct {v1, p0}, Lu64;-><init>(Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;)V

    .line 15
    .line 16
    .line 17
    iput-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f:Lu64;

    .line 18
    .line 19
    goto :goto_0

    .line 20
    :catchall_0
    move-exception p0

    .line 21
    goto :goto_1

    .line 22
    :cond_0
    :goto_0
    monitor-exit v0

    .line 23
    goto :goto_2

    .line 24
    :goto_1
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    .line 25
    throw p0

    .line 26
    :cond_1
    :goto_2
    iget-object p0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f:Lu64;

    .line 27
    .line 28
    invoke-virtual {p0}, Lu64;->a()Ljava/lang/Object;

    .line 29
    .line 30
    .line 31
    move-result-object p0

    .line 32
    return-object p0
.end method

.method public final c()Ll83;
    .locals 11

    .line 1
    new-instance v0, Landroid/content/Intent;

    .line 2
    .line 3
    const-class v1, Lcom/isaakhanimann/journal/MainActivity;

    .line 4
    .line 5
    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 6
    .line 7
    .line 8
    const-string v1, "com.isaakhanimann.journal.timeline.ADD_INGESTION"

    .line 9
    .line 10
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    .line 11
    .line 12
    .line 13
    const-string v1, "open_add_ingestion"

    .line 14
    .line 15
    const/4 v2, 0x1

    .line 16
    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    .line 17
    .line 18
    .line 19
    const/high16 v1, 0x24000000

    .line 20
    .line 21
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    .line 22
    .line 23
    .line 24
    const/4 v1, 0x3

    .line 25
    const/high16 v2, 0xc000000

    .line 26
    .line 27
    invoke-static {p0, v1, v0, v2}, Landroid/app/PendingIntent;->getActivity(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;

    .line 28
    .line 29
    .line 30
    move-result-object v6

    .line 31
    invoke-virtual {v6}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 32
    .line 33
    .line 34
    new-instance v7, Landroid/os/Bundle;

    .line 35
    .line 36
    invoke-direct {v7}, Landroid/os/Bundle;-><init>()V

    .line 37
    .line 38
    .line 39
    const-string p0, "\uc12d\ucde8 \ucd94\uac00"

    .line 40
    .line 41
    invoke-static {p0}, Ln83;->b(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;

    .line 42
    .line 43
    .line 44
    move-result-object v5

    .line 45
    new-instance p0, Ljava/util/ArrayList;

    .line 46
    .line 47
    invoke-direct {p0}, Ljava/util/ArrayList;-><init>()V

    .line 48
    .line 49
    .line 50
    new-instance v0, Ljava/util/ArrayList;

    .line 51
    .line 52
    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    .line 53
    .line 54
    .line 55
    invoke-virtual {p0}, Ljava/util/ArrayList;->isEmpty()Z

    .line 56
    .line 57
    .line 58
    move-result v1

    .line 59
    if-eqz v1, :cond_0

    .line 60
    .line 61
    goto :goto_0

    .line 62
    :cond_0
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    .line 63
    .line 64
    .line 65
    move-result v1

    .line 66
    new-array v1, v1, [Lgu3;

    .line 67
    .line 68
    invoke-virtual {p0, v1}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    .line 69
    .line 70
    .line 71
    move-result-object p0

    .line 72
    check-cast p0, [Lgu3;

    .line 73
    .line 74
    :goto_0
    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    .line 75
    .line 76
    .line 77
    move-result p0

    .line 78
    if-eqz p0, :cond_1

    .line 79
    .line 80
    const/4 p0, 0x0

    .line 81
    :goto_1
    move-object v8, p0

    .line 82
    goto :goto_2

    .line 83
    :cond_1
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    .line 84
    .line 85
    .line 86
    move-result p0

    .line 87
    new-array p0, p0, [Lgu3;

    .line 88
    .line 89
    invoke-virtual {v0, p0}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    .line 90
    .line 91
    .line 92
    move-result-object p0

    .line 93
    check-cast p0, [Lgu3;

    .line 94
    .line 95
    goto :goto_1

    .line 96
    :goto_2
    new-instance v3, Ll83;

    .line 97
    .line 98
    const/4 v4, 0x0

    .line 99
    const/4 v9, 0x1

    .line 100
    move v10, v9

    .line 101
    invoke-direct/range {v3 .. v10}, Ll83;-><init>(Landroidx/core/graphics/drawable/IconCompat;Ljava/lang/CharSequence;Landroid/app/PendingIntent;Landroid/os/Bundle;[Lgu3;ZZ)V

    .line 102
    .line 103
    .line 104
    return-object v3
.end method

.method public final d()Lrh1;
    .locals 0

    .line 1
    iget-object p0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->k:Lrh1;

    .line 2
    .line 3
    if-eqz p0, :cond_0

    .line 4
    .line 5
    return-object p0

    .line 6
    :cond_0
    const-string p0, "experienceRepo"

    .line 7
    .line 8
    invoke-static {p0}, Llb2;->N(Ljava/lang/String;)V

    .line 9
    .line 10
    .line 11
    const/4 p0, 0x0

    .line 12
    throw p0
.end method

.method public final e()V
    .locals 5

    .line 1
    iget-boolean v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->h:Z

    .line 2
    .line 3
    if-nez v0, :cond_0

    .line 4
    .line 5
    const/4 v0, 0x1

    .line 6
    iput-boolean v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->h:Z

    .line 7
    .line 8
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->a()Ljava/lang/Object;

    .line 9
    .line 10
    .line 11
    move-result-object v0

    .line 12
    check-cast v0, Llw4;

    .line 13
    .line 14
    check-cast v0, Ldu0;

    .line 15
    .line 16
    iget-object v0, v0, Ldu0;->a:Lfu0;

    .line 17
    .line 18
    new-instance v1, Lw64;

    .line 19
    .line 20
    iget-object v2, v0, Lfu0;->e:Lwp3;

    .line 21
    .line 22
    invoke-interface {v2}, Lvp3;->get()Ljava/lang/Object;

    .line 23
    .line 24
    .line 25
    move-result-object v2

    .line 26
    check-cast v2, Lrh1;

    .line 27
    .line 28
    iget-object v3, v0, Lfu0;->k:Lwp3;

    .line 29
    .line 30
    invoke-interface {v3}, Lvp3;->get()Ljava/lang/Object;

    .line 31
    .line 32
    .line 33
    move-result-object v3

    .line 34
    check-cast v3, Lit3;

    .line 35
    .line 36
    iget-object v4, v0, Lfu0;->m:Lwp3;

    .line 37
    .line 38
    invoke-interface {v4}, Lvp3;->get()Ljava/lang/Object;

    .line 39
    .line 40
    .line 41
    move-result-object v4

    .line 42
    check-cast v4, Lc75;

    .line 43
    .line 44
    invoke-direct {v1, v2, v3, v4}, Lw64;-><init>(Lrh1;Lit3;Lc75;)V

    .line 45
    .line 46
    .line 47
    iput-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->i:Lw64;

    .line 48
    .line 49
    new-instance v1, Lfk;

    .line 50
    .line 51
    iget-object v2, v0, Lfu0;->a:Lfk;

    .line 52
    .line 53
    iget-object v2, v2, Lfk;->f:Landroid/content/Context;

    .line 54
    .line 55
    const/4 v3, 0x0

    .line 56
    invoke-direct {v1, v2, v3}, Lfk;-><init>(Landroid/content/Context;B)V

    .line 57
    .line 58
    .line 59
    iput-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->j:Lfk;

    .line 60
    .line 61
    iget-object v1, v0, Lfu0;->e:Lwp3;

    .line 62
    .line 63
    invoke-interface {v1}, Lvp3;->get()Ljava/lang/Object;

    .line 64
    .line 65
    .line 66
    move-result-object v1

    .line 67
    check-cast v1, Lrh1;

    .line 68
    .line 69
    iput-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->k:Lrh1;

    .line 70
    .line 71
    iget-object v0, v0, Lfu0;->m:Lwp3;

    .line 72
    .line 73
    invoke-interface {v0}, Lvp3;->get()Ljava/lang/Object;

    .line 74
    .line 75
    .line 76
    move-result-object v0

    .line 77
    check-cast v0, Lc75;

    .line 78
    .line 79
    iput-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->l:Lc75;

    .line 80
    .line 81
    :cond_0
    invoke-super {p0}, Landroid/app/Service;->onCreate()V

    .line 82
    .line 83
    .line 84
    return-void
.end method

.method public final f(I)Landroid/app/PendingIntent;
    .locals 2

    .line 1
    new-instance v0, Landroid/content/Intent;

    .line 2
    .line 3
    const-class v1, Lcom/isaakhanimann/journal/MainActivity;

    .line 4
    .line 5
    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 6
    .line 7
    .line 8
    const-string v1, "com.isaakhanimann.journal.timeline.OPEN_EXPERIENCE"

    .line 9
    .line 10
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    .line 11
    .line 12
    .line 13
    const-string v1, "open_experience_id"

    .line 14
    .line 15
    invoke-virtual {v0, v1, p1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    .line 16
    .line 17
    .line 18
    const/high16 p1, 0x24000000

    .line 19
    .line 20
    invoke-virtual {v0, p1}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    .line 21
    .line 22
    .line 23
    const/high16 p1, 0xc000000

    .line 24
    .line 25
    const/4 v1, 0x1

    .line 26
    invoke-static {p0, v1, v0, p1}, Landroid/app/PendingIntent;->getActivity(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;

    .line 27
    .line 28
    .line 29
    move-result-object p0

    .line 30
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 31
    .line 32
    .line 33
    return-object p0
.end method

.method public final g()Ll83;
    .locals 11

    .line 1
    new-instance v0, Landroid/content/Intent;

    .line 2
    .line 3
    const-class v1, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;

    .line 4
    .line 5
    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 6
    .line 7
    .line 8
    const-string v1, "com.isaakhanimann.journal.timeline.STOP"

    .line 9
    .line 10
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    .line 11
    .line 12
    .line 13
    const/4 v1, 0x2

    .line 14
    const/high16 v2, 0xc000000

    .line 15
    .line 16
    invoke-static {p0, v1, v0, v2}, Landroid/app/PendingIntent;->getService(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;

    .line 17
    .line 18
    .line 19
    move-result-object v6

    .line 20
    invoke-virtual {v6}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 21
    .line 22
    .line 23
    new-instance v7, Landroid/os/Bundle;

    .line 24
    .line 25
    invoke-direct {v7}, Landroid/os/Bundle;-><init>()V

    .line 26
    .line 27
    .line 28
    const-string p0, "\uc911\uc9c0"

    .line 29
    .line 30
    invoke-static {p0}, Ln83;->b(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;

    .line 31
    .line 32
    .line 33
    move-result-object v5

    .line 34
    new-instance p0, Ljava/util/ArrayList;

    .line 35
    .line 36
    invoke-direct {p0}, Ljava/util/ArrayList;-><init>()V

    .line 37
    .line 38
    .line 39
    new-instance v0, Ljava/util/ArrayList;

    .line 40
    .line 41
    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    .line 42
    .line 43
    .line 44
    invoke-virtual {p0}, Ljava/util/ArrayList;->isEmpty()Z

    .line 45
    .line 46
    .line 47
    move-result v1

    .line 48
    if-eqz v1, :cond_0

    .line 49
    .line 50
    goto :goto_0

    .line 51
    :cond_0
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    .line 52
    .line 53
    .line 54
    move-result v1

    .line 55
    new-array v1, v1, [Lgu3;

    .line 56
    .line 57
    invoke-virtual {p0, v1}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    .line 58
    .line 59
    .line 60
    move-result-object p0

    .line 61
    check-cast p0, [Lgu3;

    .line 62
    .line 63
    :goto_0
    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    .line 64
    .line 65
    .line 66
    move-result p0

    .line 67
    if-eqz p0, :cond_1

    .line 68
    .line 69
    const/4 p0, 0x0

    .line 70
    :goto_1
    move-object v8, p0

    .line 71
    goto :goto_2

    .line 72
    :cond_1
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    .line 73
    .line 74
    .line 75
    move-result p0

    .line 76
    new-array p0, p0, [Lgu3;

    .line 77
    .line 78
    invoke-virtual {v0, p0}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    .line 79
    .line 80
    .line 81
    move-result-object p0

    .line 82
    check-cast p0, [Lgu3;

    .line 83
    .line 84
    goto :goto_1

    .line 85
    :goto_2
    new-instance v3, Ll83;

    .line 86
    .line 87
    const/4 v4, 0x0

    .line 88
    const/4 v9, 0x1

    .line 89
    move v10, v9

    .line 90
    invoke-direct/range {v3 .. v10}, Ll83;-><init>(Landroidx/core/graphics/drawable/IconCompat;Ljava/lang/CharSequence;Landroid/app/PendingIntent;Landroid/os/Bundle;[Lgu3;ZZ)V

    .line 91
    .line 92
    .line 93
    return-object v3
.end method

.method public final h()V
    .locals 3

    .line 1
    iget-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->n:Lqf4;

    .line 2
    .line 3
    const/4 v1, 0x0

    .line 4
    if-eqz v0, :cond_0

    .line 5
    .line 6
    invoke-virtual {v0, v1}, Lvc2;->g(Ljava/util/concurrent/CancellationException;)V

    .line 7
    .line 8
    .line 9
    :cond_0
    iput-object v1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->n:Lqf4;

    .line 10
    .line 11
    iget-boolean v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->o:Z

    .line 12
    .line 13
    if-eqz v0, :cond_1

    .line 14
    .line 15
    return-void

    .line 16
    :cond_1
    const/4 v0, 0x1

    .line 17
    iput-boolean v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->o:Z

    .line 18
    .line 19
    sget-object v0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->p:Log4;

    .line 20
    .line 21
    invoke-virtual {v0, v1}, Log4;->i(Ljava/lang/Object;)V

    .line 22
    .line 23
    .line 24
    new-instance v0, Lly;

    .line 25
    .line 26
    const/16 v2, 0x9

    .line 27
    .line 28
    invoke-direct {v0, p0, v1, v2}, Lly;-><init>(Ljava/lang/Object;Lip0;I)V

    .line 29
    .line 30
    .line 31
    const/4 v2, 0x3

    .line 32
    iget-object p0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->m:Lep0;

    .line 33
    .line 34
    invoke-static {p0, v1, v0, v2}, Lkb3;->s(Lvq0;Lmq0;Lev1;I)Lqf4;

    .line 35
    .line 36
    .line 37
    return-void
.end method

.method public final onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .locals 0

    .line 1
    const/4 p0, 0x0

    .line 2
    return-object p0
.end method

.method public final onCreate()V
    .locals 4

    .line 1
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->e()V

    .line 2
    .line 3
    .line 4
    new-instance v0, Landroid/app/NotificationChannel;

    .line 5
    .line 6
    const-string v1, "\ud0c0\uc784\ub77c\uc778 \uc54c\ub9bc"

    .line 7
    .line 8
    const/4 v2, 0x2

    .line 9
    const-string v3, "live_timeline"

    .line 10
    .line 11
    invoke-direct {v0, v3, v1, v2}, Landroid/app/NotificationChannel;-><init>(Ljava/lang/String;Ljava/lang/CharSequence;I)V

    .line 12
    .line 13
    .line 14
    const-string v1, "\ud65c\uc131 \uc800\ub110 \ud0c0\uc784\ub77c\uc778\uc744 \ud45c\uc2dc\ud569\ub2c8\ub2e4."

    .line 15
    .line 16
    invoke-virtual {v0, v1}, Landroid/app/NotificationChannel;->setDescription(Ljava/lang/String;)V

    .line 17
    .line 18
    .line 19
    const-class v1, Landroid/app/NotificationManager;

    .line 20
    .line 21
    invoke-virtual {p0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    .line 22
    .line 23
    .line 24
    move-result-object p0

    .line 25
    check-cast p0, Landroid/app/NotificationManager;

    .line 26
    .line 27
    invoke-virtual {p0, v0}, Landroid/app/NotificationManager;->createNotificationChannel(Landroid/app/NotificationChannel;)V

    .line 28
    .line 29
    .line 30
    return-void
.end method

.method public final onDestroy()V
    .locals 2

    .line 1
    iget-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->n:Lqf4;

    .line 2
    .line 3
    const/4 v1, 0x0

    .line 4
    if-eqz v0, :cond_0

    .line 5
    .line 6
    invoke-virtual {v0, v1}, Lvc2;->g(Ljava/util/concurrent/CancellationException;)V

    .line 7
    .line 8
    .line 9
    :cond_0
    sget-object v0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->p:Log4;

    .line 10
    .line 11
    invoke-virtual {v0, v1}, Log4;->i(Ljava/lang/Object;)V

    .line 12
    .line 13
    .line 14
    iget-object v0, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->m:Lep0;

    .line 15
    .line 16
    invoke-static {v0, v1}, Lu40;->u(Lvq0;Ljava/util/concurrent/CancellationException;)V

    .line 17
    .line 18
    .line 19
    invoke-super {p0}, Landroid/app/Service;->onDestroy()V

    .line 20
    .line 21
    .line 22
    return-void
.end method

.method public final onStartCommand(Landroid/content/Intent;II)I
    .locals 6

    .line 1
    const/4 v4, 0x0

    .line 2
    if-eqz p1, :cond_0

    .line 3
    .line 4
    invoke-virtual {p1}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    .line 5
    .line 6
    .line 7
    move-result-object p2

    .line 8
    goto :goto_0

    .line 9
    :cond_0
    move-object p2, v4

    .line 10
    :goto_0
    const/4 p3, 0x2

    .line 11
    if-eqz p2, :cond_5

    .line 12
    .line 13
    invoke-virtual {p2}, Ljava/lang/String;->hashCode()I

    .line 14
    .line 15
    .line 16
    move-result v0

    .line 17
    const v1, 0xb0c2097

    .line 18
    .line 19
    .line 20
    if-eq v0, v1, :cond_4

    .line 21
    .line 22
    const v1, 0x1855951e

    .line 23
    .line 24
    .line 25
    if-eq v0, v1, :cond_3

    .line 26
    .line 27
    const p1, 0x5b9faba6

    .line 28
    .line 29
    .line 30
    if-eq v0, p1, :cond_1

    .line 31
    .line 32
    goto :goto_1

    .line 33
    :cond_1
    const-string p1, "com.isaakhanimann.journal.timeline.STOP"

    .line 34
    .line 35
    invoke-virtual {p2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    .line 36
    .line 37
    .line 38
    move-result p1

    .line 39
    if-nez p1, :cond_2

    .line 40
    .line 41
    goto :goto_1

    .line 42
    :cond_2
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->h()V

    .line 43
    .line 44
    .line 45
    return p3

    .line 46
    :cond_3
    const-string v0, "com.isaakhanimann.journal.timeline.START"

    .line 47
    .line 48
    invoke-virtual {p2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    .line 49
    .line 50
    .line 51
    move-result p2

    .line 52
    if-nez p2, :cond_5

    .line 53
    .line 54
    goto :goto_1

    .line 55
    :cond_4
    const-string v0, "com.isaakhanimann.journal.timeline.REFRESH"

    .line 56
    .line 57
    invoke-virtual {p2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    .line 58
    .line 59
    .line 60
    move-result p2

    .line 61
    if-nez p2, :cond_5

    .line 62
    .line 63
    :goto_1
    return p3

    .line 64
    :cond_5
    const/4 p2, -0x1

    .line 65
    if-eqz p1, :cond_6

    .line 66
    .line 67
    const-string v0, "experience_id"

    .line 68
    .line 69
    invoke-virtual {p1, v0, p2}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    .line 70
    .line 71
    .line 72
    move-result v0

    .line 73
    move v2, v0

    .line 74
    goto :goto_2

    .line 75
    :cond_6
    move v2, p2

    .line 76
    :goto_2
    if-eqz p1, :cond_7

    .line 77
    .line 78
    const-string v0, "consumer_name"

    .line 79
    .line 80
    invoke-virtual {p1, v0}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;

    .line 81
    .line 82
    .line 83
    move-result-object p1

    .line 84
    goto :goto_3

    .line 85
    :cond_7
    move-object p1, v4

    .line 86
    :goto_3
    if-nez p1, :cond_8

    .line 87
    .line 88
    const-string p1, ""

    .line 89
    .line 90
    :cond_8
    move-object v3, p1

    .line 91
    if-eq v2, p2, :cond_9

    .line 92
    .line 93
    invoke-static {v3}, Lgj4;->m0(Ljava/lang/CharSequence;)Z

    .line 94
    .line 95
    .line 96
    move-result p1

    .line 97
    if-eqz p1, :cond_a

    .line 98
    .line 99
    :cond_9
    move-object v1, p0

    .line 100
    goto/16 :goto_5

    .line 101
    .line 102
    :cond_a
    const/4 p1, 0x0

    .line 103
    iput-boolean p1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->o:Z

    .line 104
    .line 105
    new-instance p1, Ln83;

    .line 106
    .line 107
    const-string p2, "live_timeline"

    .line 108
    .line 109
    invoke-direct {p1, p0, p2}, Ln83;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    .line 110
    .line 111
    .line 112
    const p2, 0x7f08005a

    .line 113
    .line 114
    .line 115
    iget-object v0, p1, Ln83;->q:Landroid/app/Notification;

    .line 116
    .line 117
    iput p2, v0, Landroid/app/Notification;->icon:I

    .line 118
    .line 119
    const-string p2, "\ud0c0\uc784\ub77c\uc778 \uc54c\ub9bc"

    .line 120
    .line 121
    invoke-static {p2}, Ln83;->b(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;

    .line 122
    .line 123
    .line 124
    move-result-object p2

    .line 125
    iput-object p2, p1, Ln83;->e:Ljava/lang/CharSequence;

    .line 126
    .line 127
    const-string p2, "\ud6a8\uacfc \ud0c0\uc784\ub77c\uc778 \uc900\ube44 \uc911"

    .line 128
    .line 129
    invoke-static {p2}, Ln83;->b(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;

    .line 130
    .line 131
    .line 132
    move-result-object p2

    .line 133
    iput-object p2, p1, Ln83;->f:Ljava/lang/CharSequence;

    .line 134
    .line 135
    invoke-virtual {p0, v2}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->f(I)Landroid/app/PendingIntent;

    .line 136
    .line 137
    .line 138
    move-result-object p2

    .line 139
    iput-object p2, p1, Ln83;->g:Landroid/app/PendingIntent;

    .line 140
    .line 141
    const/4 p2, 0x1

    .line 142
    iput-boolean p2, p1, Ln83;->k:Z

    .line 143
    .line 144
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->c()Ll83;

    .line 145
    .line 146
    .line 147
    move-result-object v0

    .line 148
    iget-object v1, p1, Ln83;->b:Ljava/util/ArrayList;

    .line 149
    .line 150
    invoke-virtual {v1, v0}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 151
    .line 152
    .line 153
    invoke-virtual {p0}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->g()Ll83;

    .line 154
    .line 155
    .line 156
    move-result-object v0

    .line 157
    invoke-virtual {v1, v0}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 158
    .line 159
    .line 160
    invoke-virtual {p1, p3}, Ln83;->c(I)V

    .line 161
    .line 162
    .line 163
    const/16 v0, 0x8

    .line 164
    .line 165
    invoke-virtual {p1, v0}, Ln83;->c(I)V

    .line 166
    .line 167
    .line 168
    iput-boolean p2, p1, Ln83;->r:Z

    .line 169
    .line 170
    invoke-virtual {p1}, Ln83;->a()Landroid/app/Notification;

    .line 171
    .line 172
    .line 173
    move-result-object p1

    .line 174
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 175
    .line 176
    .line 177
    sget p2, Landroid/os/Build$VERSION;->SDK_INT:I

    .line 178
    .line 179
    const v0, 0xafc9

    .line 180
    .line 181
    .line 182
    const/16 v1, 0x22

    .line 183
    .line 184
    if-lt p2, v1, :cond_d

    .line 185
    .line 186
    if-lt p2, v1, :cond_b

    .line 187
    .line 188
    invoke-static {p0, p1}, Lhq;->o(Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;Landroid/app/Notification;)V

    .line 189
    .line 190
    .line 191
    goto :goto_4

    .line 192
    :cond_b
    const/16 v1, 0x1d

    .line 193
    .line 194
    if-lt p2, v1, :cond_c

    .line 195
    .line 196
    invoke-static {p0, p1}, Lhq;->n(Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;Landroid/app/Notification;)V

    .line 197
    .line 198
    .line 199
    goto :goto_4

    .line 200
    :cond_c
    invoke-virtual {p0, v0, p1}, Landroid/app/Service;->startForeground(ILandroid/app/Notification;)V

    .line 201
    .line 202
    .line 203
    goto :goto_4

    .line 204
    :cond_d
    invoke-virtual {p0, v0, p1}, Landroid/app/Service;->startForeground(ILandroid/app/Notification;)V

    .line 205
    .line 206
    .line 207
    :goto_4
    iget-object p1, p0, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->n:Lqf4;

    .line 208
    .line 209
    if-eqz p1, :cond_e

    .line 210
    .line 211
    invoke-virtual {p1, v4}, Lvc2;->g(Ljava/util/concurrent/CancellationException;)V

    .line 212
    .line 213
    .line 214
    :cond_e
    new-instance p1, Lj3;

    .line 215
    .line 216
    invoke-direct {p1, v2, v3}, Lj3;-><init>(ILjava/lang/String;)V

    .line 217
    .line 218
    .line 219
    sget-object p2, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->p:Log4;

    .line 220
    .line 221
    invoke-virtual {p2}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    .line 222
    .line 223
    .line 224
    invoke-virtual {p2, v4, p1}, Log4;->j(Ljava/lang/Object;Ljava/lang/Object;)Z

    .line 225
    .line 226
    .line 227
    new-instance v0, Lp9;

    .line 228
    .line 229
    const/16 v5, 0x8

    .line 230
    .line 231
    move-object v1, p0

    .line 232
    invoke-direct/range {v0 .. v5}, Lp9;-><init>(Ljava/lang/Object;ILjava/lang/Object;Lip0;I)V

    .line 233
    .line 234
    .line 235
    const/4 p0, 0x3

    .line 236
    iget-object p1, v1, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->m:Lep0;

    .line 237
    .line 238
    invoke-static {p1, v4, v0, p0}, Lkb3;->s(Lvq0;Lmq0;Lev1;I)Lqf4;

    .line 239
    .line 240
    .line 241
    move-result-object p0

    .line 242
    iput-object p0, v1, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->n:Lqf4;

    .line 243
    .line 244
    return p3

    .line 245
    :goto_5
    invoke-virtual {v1}, Lcom/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService;->h()V

    .line 246
    .line 247
    .line 248
    return p3
.end method
